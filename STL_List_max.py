import streamlit as st

# Function to find the largest number without using max()
def find_largest(lst):
    if not lst:
        return "List is empty!"
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

# Streamlit UI
st.title("🔍 Find the Largest Number in a List (Without max())")

user_input = st.text_input("Enter numbers separated by commas (e.g., 3, 7, 2, 9):")

if user_input:
    try:
        # Convert string to list of integers
        num_list = [int(x.strip()) for x in user_input.split(",")]
        result = find_largest(num_list)
        st.success(f"The largest number is: {result}")
    except ValueError:
        st.error("Please enter only numbers separated by commas.")
