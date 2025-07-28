# app.py

import streamlit as st
from number_utils import is_positive, is_even, is_prime

st.title("🔢 Number Checker")

# User input
number = st.number_input("Enter a number:", value=0, step=1)

# Button to evaluate
if st.button("Check Number"):
    st.write(f"✅ Positive: {'Yes' if is_positive(number) else 'No'}")
    st.write(f"✅ Even: {'Yes' if is_even(number) else 'No'}")
    st.write(f"✅ Prime: {'Yes' if is_prime(number) else 'No'}")
