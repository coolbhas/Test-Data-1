import streamlit as st
from area_utils import area_of_circle, area_of_rectangle, area_of_triangle

st.title("🧮 Area Calculator")

shape = st.selectbox("Choose a shape", ["Circle", "Rectangle", "Triangle"])

try:
    if shape == "Circle":
        radius = st.number_input("Enter radius", min_value=0.0, step=0.1)
        if st.button("Calculate Area"):
            result = area_of_circle(radius)
            st.success(f"Area of the circle: {result:.2f}")

    elif shape == "Rectangle":
        length = st.number_input("Enter length", min_value=0.0, step=0.1)
        width = st.number_input("Enter width", min_value=0.0, step=0.1)
        if st.button("Calculate Area"):
            result = area_of_rectangle(length, width)
            st.success(f"Area of the rectangle: {result:.2f}")

    elif shape == "Triangle":
        base = st.number_input("Enter base", min_value=0.0, step=0.1)
        height = st.number_input("Enter height", min_value=0.0, step=0.1)
        if st.button("Calculate Area"):
            result = area_of_triangle(base, height)
            st.success(f"Area of the triangle: {result:.2f}")
except ValueError as e:
    st.error(f"Error: {e}")
