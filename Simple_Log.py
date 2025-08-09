# app.py
from pathlib import Path
from datetime import datetime
import streamlit as st

# --- config ---
LOG_DIR = Path.cwd() / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "simple_log.txt"

# --- helpers ---
def append_log(message: str) -> None:
    msg = message.strip()
    if not msg:
        return
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{ts} - {msg}\n")

def read_logs() -> str:
    if not LOG_FILE.exists():
        return ""
    return LOG_FILE.read_text(encoding="utf-8")

# --- UI ---
st.set_page_config(page_title="Simple Log", page_icon="📝")
st.title("Simple Log — daily activity logger")

with st.form("add_entry"):
    activity = st.text_input("What did you do?", placeholder="e.g. Reviewed project proposal")
    submitted = st.form_submit_button("Add to log")
    if submitted:
        if activity.strip():
            append_log(activity)
            st.success("Saved to log.")
        else:
            st.warning("Please type an activity before submitting.")

st.markdown("---")
st.subheader("Recent entries")
logs_text = read_logs()
if logs_text:
    st.code(logs_text, language="text")
else:
    st.info("No entries yet — add the first activity above.")

st.download_button("Download logs", data=logs_text, file_name="simple_log.txt", mime="text/plain")

if st.button("Clear logs"):
    LOG_FILE.write_text("", encoding="utf-8")
    st.experimental_rerun()
