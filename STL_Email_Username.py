import streamlit as st

# Function to extract username from email
def extract_username(email):
    email = email.strip()
    if "@" not in email or email.count("@") != 1:
        return None
    username = email.split("@")[0]
    return username if username else None

# Streamlit UI
st.title("📧 Email Username Extractor")

email_input = st.text_input("Enter your email address:")

if st.button("Extract Username"):
    result = extract_username(email_input)
    if result:
        st.success(f"Username extracted: **{result}**")
    else:
        st.error("Invalid email format. Please enter a valid email.")
