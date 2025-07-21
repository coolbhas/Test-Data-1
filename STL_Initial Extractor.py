import streamlit as st

# Function to extract initials from full name
def extract_initials(full_name: str) -> str:
    if not full_name.strip():
        return "Invalid Input"
    # Remove extra spaces, split the name into parts
    words = full_name.strip().split()
    initials = [word[0].upper() for word in words if word]
    return ".".join(initials)

# Streamlit UI
st.set_page_config(page_title="Initial Extractor", page_icon="🔤", layout="centered")
st.title("🔤 Initial Extractor")
st.write("Extract initials from a full name using dot-separated uppercase format.")

# Input field
full_name = st.text_input("Enter Full Name:")

# Process and display output
if st.button("Extract Initials"):
    result = extract_initials(full_name)
    st.success(f"Initials: **{result}**")
