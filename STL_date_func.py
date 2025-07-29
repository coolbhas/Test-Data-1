import streamlit as st
from datetime import datetime, date

# --- Utility Functions ---
def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_age(birthdate: str, date_format: str = "%Y-%m-%d") -> int:
    birth = datetime.strptime(birthdate, date_format).date()
    today = date.today()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    return age

# --- Streamlit UI ---
st.title("🗓️ Date Utility Functions")

tab1, tab2 = st.tabs(["Check Leap Year", "Calculate Age"])

with tab1:
    st.header("Leap Year Checker")
    year_input = st.number_input("Enter Year", min_value=1, max_value=9999, value=2024)
    if st.button("Check Leap Year"):
        if is_leap_year(year_input):
            st.success(f"✅ {year_input} is a Leap Year.")
        else:
            st.error(f"❌ {year_input} is NOT a Leap Year.")

with tab2:
    st.header("Age Calculator")
    birth_date = st.date_input("Select your Birth Date", min_value=date(1900, 1, 1))
    if st.button("Calculate Age"):
        age = calculate_age(str(birth_date))
        st.info(f"🎉 You are {age} years old.")
