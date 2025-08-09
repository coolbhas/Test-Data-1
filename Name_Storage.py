from pathlib import Path
import streamlit as st

# file where names are stored
FILE_PATH = Path("names.txt")

def ensure_file():
    FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not FILE_PATH.exists():
        FILE_PATH.write_text("", encoding="utf-8")

def save_name(name: str):
    name = (name or "").strip()
    if not name:
        return False, "Please enter a non-empty name."
    ensure_file()
    try:
        with FILE_PATH.open("a", encoding="utf-8") as f:
            f.write(name + "\n")
        return True, f"Saved: {name}"
    except Exception as e:
        return False, f"Error saving name: {e}"

def read_names():
    if not FILE_PATH.exists():
        return []
    try:
        with FILE_PATH.open("r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except Exception:
        return []

def clear_names():
    if FILE_PATH.exists():
        FILE_PATH.unlink()
    return []

def main():
    st.set_page_config(page_title="Name Storage", layout="centered")
    st.title("Name Storage")
    st.write("Save names to a file and read them back.")

    # Initialize state
    if "names" not in st.session_state:
        st.session_state.names = read_names()

    # Form for adding names
    with st.form("add_name_form", clear_on_submit=True):
        name = st.text_input("Enter name")
        submit = st.form_submit_button("Save Name")
        if submit:
            ok, msg = save_name(name)
            if ok:
                st.success(msg)
                st.session_state.names = read_names()
            else:
                st.error(msg)

    st.markdown("---")
    st.subheader("Stored Names")
    if st.session_state.names:
        st.write(f"Total: {len(st.session_state.names)}")
        st.table([{"#": i+1, "Name": n} for i, n in enumerate(st.session_state.names)])
    else:
        st.info("No names stored yet.")

    st.markdown("---")
    cols = st.columns([1, 1, 1])
    if cols[0].button("Refresh"):
        st.session_state.names = read_names()
        st.experimental_rerun()
    if cols[1].button("Export to CSV"):
        csv = "name\n" + "\n".join(st.session_state.names)
        st.download_button("Download CSV", csv, file_name="names.csv", mime="text/csv")
    if cols[2].button("Clear All"):
        clear_names()
        st.session_state.names = []
        st.success("All names cleared.")

if __name__ == "__main__":
    main()
