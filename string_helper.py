# app.py

import streamlit as st
import string_utils as su

st.title("🧵 String Helper Functions")

input_text = st.text_input("Enter a string:")

if input_text:
    st.subheader("Results:")
    st.write(f"Capitalized: `{su.capitalize_string(input_text)}`")
    st.write(f"Reversed: `{su.reverse_string(input_text)}`")
    st.write(f"Character Count: `{su.count_characters(input_text)}`")
    st.write(f"Without Whitespace: `{su.remove_whitespace(input_text)}`")
    st.write(f"Is Palindrome? `{su.is_palindrome(input_text)}`")
    st.write(f"Vowel Count: `{su.count_vowels(input_text)}`")
