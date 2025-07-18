import streamlit as st

# Title of the app
st.title("🔁 Word Reverser")

# User input
sentence = st.text_input("Enter a sentence:")

# Function to reverse each word in the sentence
def reverse_words(sentence: str) -> str:
    return ' '.join(word[::-1] for word in sentence.split())

# When user enters text
if sentence:
    reversed_output = reverse_words(sentence)
    st.success(f"Reversed Sentence: {reversed_output}")
