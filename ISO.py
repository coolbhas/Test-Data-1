
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text()
    return full_text
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from rag_engine import build_vector_store, load_vector_store, get_adaptive_qa_chain

import os

# Load or create vector DB
def build_vector_store(text, store_path="vector_store"):
    embeddings = OpenAIEmbeddings()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = splitter.create_documents([text])
    vectordb = FAISS.from_documents(docs, embeddings)
    vectordb.save_local(store_path)
    return vectordb

def load_vector_store(store_path="vector_store"):
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(store_path, embeddings)

# Adaptive Retrieval QA
def get_adaptive_qa_chain(vectordb, temperature=0.2):
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})
    llm = OpenAI(temperature=temperature, model_name="gpt-3.5-turbo")
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )
    return chain
import streamlit as st
from iso_parser import extract_text_from_pdf
from rag_engine import build_vector_store, load_vector_store, get_adaptive_qa_chain
import os

st.set_page_config(page_title="ISO/IEC 27001:2022 AI Assistant")

st.title("🔐 ISO/IEC 27001:2022 - Gen AI Q&A Assistant")

# Upload PDF
pdf_file = st.file_uploader("Upload ISO/IEC 27001:2022 PDF", type="pdf")

# Load PDF and process
if pdf_file:
    pdf_path = f"./{pdf_file.name}"
    with open(pdf_path, "wb") as f:
        f.write(pdf_file.getbuffer())
    
    st.success("✅ PDF Uploaded and Processing...")
    
    full_text = extract_text_from_pdf(pdf_path)
    
    if not os.path.exists("vector_store/index.faiss"):
        st.info("⚙️ Building Vector Store...")
        vectordb = build_vector_store(full_text)
    else:
        vectordb = load_vector_store()

    chain = get_adaptive_qa_chain(vectordb)

    query = st.text_input("Ask a question about ISO/IEC 27001:2022")

    if query:
        with st.spinner("Thinking..."):
            response = chain.run(query)
            st.markdown(f"**Answer:** {response}")
from dotenv import load_dotenv
load_dotenv()
