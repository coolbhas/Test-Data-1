from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun

import os
import streamlit as st
from rag_engine1 import load_pdf, query_pdf
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Gen AI Agent")
st.title("🧠 Gen AI Agent")

# Session state for file and vectorstore
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "filename" not in st.session_state:
    st.session_state.filename = None

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# Load PDF and create vectorstore
if uploaded_file:
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Uploaded: {uploaded_file.name}")
    st.session_state.vectorstore = load_pdf(uploaded_file.name)
    st.session_state.filename = uploaded_file.name

query = st.text_input("💬 Ask your question:")

if query and st.session_state.vectorstore:
    answer, docs = query_pdf(st.session_state.vectorstore, query)
    
    if "I don't have information" in answer or len(docs) == 0:
        st.warning("🤖 I don't have information on that in the provided context.")
        
        # Ask if user wants to search web
        user_decision = st.radio("Do you want me to search the web for this?", ("Yes", "No"))
        
        if user_decision == "Yes":
            search = DuckDuckGoSearchRun()
            result = search.run(query)
            st.info("🌐 Web Search Answer:")
            st.write(result)
        else:
            st.info("👍 Thank you for using Gen AI Agent. Have a good time!")
    else:
        st.markdown("📘 **Answer from PDF**")
        st.write(answer)
