import streamlit as st
import re

def calculate_text_stats(text):
    word_count = len(text.split())
    sentence_count = len(re.findall(r'[.!?]', text))
    character_count = len(text)
    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "character_count": character_count
    }

st.set_page_config(page_title="Text Statistics Tool")

st.title("📝 Text Statistics Tool")
st.write("Enter a paragraph below and get word, sentence, and character counts.")

user_input = st.text_area("Enter your paragraph here", height=200)

if st.button("Analyze"):
    if user_input.strip():
        result = calculate_text_stats(user_input)
        st.success("✅ Text analyzed successfully!")
        st.write(f"**Word Count:** {result['word_count']}")
        st.write(f"**Sentence Count:** {result['sentence_count']}")
        st.write(f"**Character Count:** {result['character_count']}")
    else:
        st.warning("⚠️ Please enter some text before analyzing.")
