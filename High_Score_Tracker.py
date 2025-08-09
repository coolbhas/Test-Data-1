# app.py
import streamlit as st
from pathlib import Path
import json
from datetime import datetime

DATA_FILE = Path(__file__).parent / "highscore.json"

def load_highscore(filepath=DATA_FILE):
    try:
        if not filepath.exists():
            return {"score": 0, "when": None}
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return {"score": int(data.get("score", 0)), "when": data.get("when")}
    except Exception as e:
        # Non-fatal: return default but show message in UI
        st.error(f"Could not load highscore file: {e}")
        return {"score": 0, "when": None}

def save_highscore(score, filepath=DATA_FILE):
    payload = {"score": int(score), "when": datetime.utcnow().isoformat() + "Z"}
    tmp = filepath.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f)
    tmp.replace(filepath)  # atomic replace

# ----- IMPORTANT: initialize session_state BEFORE creating widgets -----
if "highscore" not in st.session_state:
    st.session_state.highscore = load_highscore()["score"]

st.title("High Score Tracker")
st.write("Current high score:", st.session_state.highscore)

col1, col2 = st.columns([2, 1])
with col1:
    with st.form("score_form"):
        new_score = st.number_input("Enter latest score", min_value=0, value=0, step=1)
        submitted = st.form_submit_button("Submit Score")
        if submitted:
            if new_score > st.session_state.highscore:
                save_highscore(new_score)
                st.session_state.highscore = new_score  # OK: updating state (key not used by a widget)
                st.success(f"🎉 New high score saved: {new_score}")
            else:
                st.info(f"{new_score} did not beat the high score ({st.session_state.highscore}).")

with col2:
    if st.button("Reload from file"):
        st.session_state.highscore = load_highscore()["score"]
        st.experimental_rerun()

st.markdown("---")
data = load_highscore()
st.write("High score file:", str(DATA_FILE))
st.write("Stored score:", data["score"])
st.write("Saved at (UTC):", data["when"])
