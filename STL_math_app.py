# app.py

import streamlit as st
from math_operations import factorial, power, square_root

st.title("🧮 Math Operations Tool")

operation = st.selectbox("Choose an operation:", ["Factorial", "Power", "Square Root"])

if operation == "Factorial":
    num = st.number_input("Enter a non-negative integer", min_value=0, step=1)
    if st.button("Calculate Factorial"):
        try:
            result = factorial(int(num))
            st.success(f"Factorial of {int(num)} is {result}")
        except Exception as e:
            st.error(str(e))

elif operation == "Power":
    base = st.number_input("Enter base", value=2.0)
    exponent = st.number_input("Enter exponent", value=3.0)
    if st.button("Calculate Power"):
        try:
            result = power(base, int(exponent))
            st.success(f"{base} ^ {int(exponent)} = {result}")
        except Exception as e:
            st.error(str(e))

elif operation == "Square Root":
    number = st.number_input("Enter a non-negative number", min_value=0.0)
    if st.button("Calculate Square Root"):
        try:
            result = square_root(number)
            st.success(f"Square root of {number} ≈ {result}")
        except Exception as e:
            st.error(str(e))
