# app.py
import streamlit as st

def count_lines_words(text: str):
    lines = text.splitlines()
    total_lines = len(lines)
    total_words = sum(len(line.split()) for line in lines)  # split() ignores extra spaces
    return total_lines, total_words

st.set_page_config(page_title="Text File Reader", page_icon="📄", layout="centered")
st.title("Text File Reader")
st.write("Upload a `.txt` file. Words are counted ignoring blank/extra-space-only lines.")

uploaded_file = st.file_uploader("Choose a .txt file", type=["txt"])

if uploaded_file is not None:
    try:
        raw = uploaded_file.read()  # bytes
        # robust decode: try utf-8, fallback to latin-1, finally replace
        try:
            text = raw.decode("utf-8")
            encoding = "utf-8"
        except UnicodeDecodeError:
            try:
                text = raw.decode("latin-1")
                encoding = "latin-1"
            except Exception:
                text = raw.decode("utf-8", errors="replace")
                encoding = "utf-8 (with replacement)"

        total_lines, total_words = count_lines_words(text)

        st.markdown("### Report")
        st.write(f"**File name:** {uploaded_file.name}")
        st.write(f"**File size:** {len(raw)} bytes")
        st.write(f"**Detected encoding:** {encoding}")
        st.write(f"**Total lines:** {total_lines}")
        st.write(f"**Total words:** {total_words}")
        st.success("Processing completed!")
    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("Upload a `.txt` file to start.")
