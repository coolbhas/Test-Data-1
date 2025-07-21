import streamlit as st

def shift_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 1
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Streamlit UI
st.title("🔐 Simple Caesar Cipher - Shift by +1")
st.write("Shift each letter in your text by 1 position in the alphabet.")

user_input = st.text_area("Enter your message:")

if st.button("Encrypt"):
    encrypted = shift_cipher(user_input)
    st.success("✅ Encryption Complete!")
    st.code(f"""
Original Input: {user_input}
Ciphered Output: {encrypted}
Shift Rule: +1 position in the alphabet
Note: Non-alphabetic characters remain unchanged
    """)
