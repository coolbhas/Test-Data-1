import streamlit as st
import re

# Function to format phone number
def format_phone_number(number: str) -> str:
    digits = re.sub(r'\D', '', number)  # Remove all non-digit characters

    if len(digits) != 10:
        return "Invalid phone number: Must be exactly 10 digits"
    
    return f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"

# Streamlit UI
st.title("📞 Phone Number Formatter")

# User input
user_input = st.text_input("Enter a 10-digit phone number (with or without formatting):")

# Output section
if user_input:
    result = format_phone_number(user_input)
    st.success(f"Formatted Phone Number: {result}")
