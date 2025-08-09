"""
Number File Processor (Streamlit)

Reads numbers from an uploaded file (or pasted text), calculates sum and average,
skips invalid entries while reporting them, shows results in the UI, and allows
downloading/saving results as 'results.txt'.

Functions:
 - read_numbers_from_text(text) -> (numbers_list, invalid_list)
 - calculate_sum_and_average(numbers) -> (total, average)
 - save_results(filepath, numbers, invalid_list) -> (success, message)
"""

import streamlit as st
import re
from typing import List, Tuple

def read_numbers_from_text(text: str) -> Tuple[List[float], List[str]]:
    """
    Parse text for numeric tokens. Accepts integers and floats.
    Splits on commas and whitespace. Returns (numbers, invalid_tokens).
    """
    if not text:
        return [], []

    # split on common separators: comma, whitespace (incl newlines/tabs)
    tokens = re.split(r'[,\s]+', text)
    numbers = []
    invalid = []
    for tok in tokens:
        tok = tok.strip()
        if tok == '':
            continue
        try:
            numbers.append(float(tok))
        except ValueError:
            invalid.append(tok)
    return numbers, invalid

def calculate_sum_and_average(numbers: List[float]) -> Tuple[float, float]:
    """Return (sum, average). For empty list, return (0.0, 0.0)."""
    if not numbers:
        return 0.0, 0.0
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

def save_results(filepath: str, numbers: List[float], invalid: List[str]) -> Tuple[bool, str]:
    """Write a small report to filepath. Returns (success, message)."""
    total, avg = calculate_sum_and_average(numbers)
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"Processed {len(numbers)} valid numbers.\n")
            f.write(f"Sum: {total}\n")
            f.write(f"Average: {avg}\n")
            if invalid:
                f.write(f"Skipped {len(invalid)} invalid entries: {invalid}\n")
        return True, f"Saved results to {filepath}"
    except Exception as e:
        return False, f"Error saving file: {e}"

# ---------- Streamlit UI ----------
st.set_page_config(page_title="Number File Processor", layout="centered")

st.title("Number File Processor")
st.markdown("Upload a `.txt` or `.csv` file (numbers separated by newline, space, or commas), or paste the data below.")

uploaded_file = st.file_uploader("Upload numbers file", type=["txt", "csv"])
text_input = st.text_area("Or paste numbers here (overrides upload):", height=120)

content = None
if text_input and text_input.strip() != "":
    content = text_input
elif uploaded_file is not None:
    try:
        # decode uploaded bytes robustly
        content = uploaded_file.getvalue().decode('utf-8')
    except Exception:
        content = uploaded_file.getvalue().decode('latin-1', errors='replace')

if content is None:
    st.info("No data yet — upload a file or paste numbers.")
    st.stop()

# Process content
numbers, invalid_tokens = read_numbers_from_text(content)
total, average = calculate_sum_and_average(numbers)

# Display results
st.subheader("Results")
st.write(f"Processed **{len(numbers)}** valid numbers.")
st.write(f"**Sum:** {total}")
st.write(f"**Average:** {average}")
if invalid_tokens:
    st.warning(f"Skipped **{len(invalid_tokens)}** invalid entries: {invalid_tokens}")

# Show a sample preview of numbers
if numbers:
    # show index + value for readability
    preview = [{"index": i + 1, "value": n} for i, n in enumerate(numbers[:200])]
    st.subheader("Numbers preview (first 200)")
    st.table(preview)

# Offer download of results.txt
report_lines = [
    f"Processed {len(numbers)} valid numbers.",
    f"Sum: {total}",
    f"Average: {average}"
]
if invalid_tokens:
    report_lines.append(f"Skipped {len(invalid_tokens)} invalid entries: {invalid_tokens}")

report_text = "\n".join(report_lines) + "\n"
st.download_button("Download results.txt", data=report_text, file_name="results.txt", mime="text/plain")

# Optionally save on server filesystem (useful while developing)
if st.button("Save results to server (results.txt)"):
    success, msg = save_results("results.txt", numbers, invalid_tokens)
    if success:
        st.success(msg)
    else:
        st.error(msg)

st.markdown("---")
st.caption("Handles integers and floats. Non-numeric tokens are listed as skipped.")
