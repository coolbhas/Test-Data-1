import streamlit as st

# Function to count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# Streamlit UI
st.set_page_config(page_title="Vowel Counter", layout="centered")
st.title("🔤 Vowel Counter App")

user_input = st.text_input("Enter a word or sentence:")

if user_input:
    vowel_count = count_vowels(user_input)
    st.success(f"The number of vowels in the input is: **{vowel_count}**")

    # Report section
    st.subheader("📝 Report")
    st.write(f"Input text: {user_input}")
    st.write(f"Vowel count: {vowel_count}")
    st.write("Edge Cases handled:")
    st.markdown("- Case-insensitive vowel check\n- Empty string returns 0")

