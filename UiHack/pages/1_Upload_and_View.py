import streamlit as st
import pathlib
import pandas as pd

# --- Load CSS ---
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_path = pathlib.Path(__file__).parents[1] / "assets" / "styles.css"
load_css(css_path)

# --- Page 2 Content ---
st.markdown("<h1 class='title'>Upload & View Your File</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Drop your files below 👇</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("", type=["csv", "txt", "xlsx", "pdf"])

if uploaded_file is not None:
    st.markdown("<p class='success-msg'>✅ File uploaded successfully!</p>", unsafe_allow_html=True)

    file_details = {
        "Filename": uploaded_file.name,
        "FileType": uploaded_file.type,
        "FileSize": f"{uploaded_file.size / 1024:.2f} KB"
    }
    st.json(file_details)

    st.markdown("<h3 class='output-title'>Output</h3>", unsafe_allow_html=True)

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
    elif uploaded_file.name.endswith(".txt"):
        content = uploaded_file.read().decode("utf-8")
        st.text_area("File Content:", content, height=300)
    else:
        st.info("📁 File uploaded but preview not supported for this file type.")
