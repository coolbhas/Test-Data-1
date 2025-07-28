# app.py

import streamlit as st
from helper_functions import find_max, find_min, calculate_sum, calculate_average

st.title("List Helper Functions")

# Step 1: Get list input from user
user_input = st.text_input("Enter numbers separated by commas (e.g., 10, 20, 30)")

if user_input:
    try:
        # Step 2: Convert input to list of numbers
        number_list = [float(x.strip()) for x in user_input.split(",")]

        # Step 3: Display results using helper functions
        st.write("📊 **Results**:")
        st.write(f"🔺 Maximum: {find_max(number_list)}")
        st.write(f"🔻 Minimum: {find_min(number_list)}")
        st.write(f"➕ Sum: {calculate_sum(number_list)}")
        st.write(f"📈 Average: {calculate_average(number_list)}")

    except ValueError:
        st.error("Please enter valid numbers separated by commas.")
else:
    st.info("Awaiting input...")
