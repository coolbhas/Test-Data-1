import streamlit as st

def format_name(full_name: str):
    parts = full_name.strip().split()
    formatted = {}

    if len(parts) == 0:
        return {"Error": "No name provided."}

    # Basic Name Parts
    first = parts[0]
    last = parts[-1]
    middle = " ".join(parts[1:-1]) if len(parts) > 2 else ""

    # Derived formats
    formatted["First Last"] = f"{first} {last}"
    formatted["Last, First"] = f"{last}, {first}"
    formatted["Initials"] = ".".join([p[0].upper() for p in parts]) + "."
    formatted["Formal"] = f"Mr./Ms. {full_name}"  # Gender-neutral placeholder
    formatted["UPPERCASE"] = full_name.upper()
    formatted["lowercase"] = full_name.lower()

    return formatted

# Streamlit UI
st.title("🧑‍💼 Name Formatter Utility")

full_name = st.text_input("Enter Full Name", "")

if full_name:
    st.subheader("Formatted Output")
    results = format_name(full_name)

    if "Error" in results:
        st.error(results["Error"])
    else:
        for label, value in results.items():
            st.markdown(f"**{label}:** {value}")
