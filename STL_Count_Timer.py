import streamlit as st
import time

st.set_page_config(page_title="Countdown Timer", layout="centered")
st.title("⏳ Countdown Timer")

if 'start' not in st.session_state:
    st.session_state.start = False

if st.button("Start Countdown"):
    st.session_state.start = True
    st.session_state.seconds = 10

if st.session_state.start:
    with st.empty():
        for i in range(st.session_state.seconds, -1, -1):
            st.markdown(f"<h1 style='text-align: center;'>{i}</h1>", unsafe_allow_html=True)
            time.sleep(1)
    st.success("🎉 Time’s Up!")

