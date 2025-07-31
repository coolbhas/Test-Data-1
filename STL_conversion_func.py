import streamlit as st

# Title
st.title("🔄 Unit Conversion Tool")

# Supported units and conversion logic
def convert_units(value, from_unit, to_unit):
    # Length
    if from_unit == "feet" and to_unit == "meters":
        return round(value * 0.3048, 2)
    elif from_unit == "meters" and to_unit == "feet":
        return round(value / 0.3048, 2)

    # Weight
    elif from_unit == "pounds" and to_unit == "kilograms":
        return round(value * 0.453592, 2)
    elif from_unit == "kilograms" and to_unit == "pounds":
        return round(value / 0.453592, 2)

    # Temperature
    elif from_unit == "celsius" and to_unit == "fahrenheit":
        return round((value * 9/5) + 32, 2)
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return round((value - 32) * 5/9, 2)

    # Distance
    elif from_unit == "kilometers" and to_unit == "miles":
        return round(value * 0.621371, 2)
    elif from_unit == "miles" and to_unit == "kilometers":
        return round(value / 0.621371, 2)

    else:
        return "❌ Conversion not supported."

# Input fields
value = st.number_input("Enter value to convert", min_value=0.0)
from_unit = st.selectbox("From Unit", ["feet", "meters", "pounds", "kilograms", "celsius", "fahrenheit", "kilometers", "miles"])
to_unit = st.selectbox("To Unit", ["feet", "meters", "pounds", "kilograms", "celsius", "fahrenheit", "kilometers", "miles"])

# Button
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} is equal to {result} {to_unit}")
