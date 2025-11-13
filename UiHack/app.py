import streamlit as st
import time
import pandas as pd
import pathlib

# --- Load CSS ---
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_path = pathlib.Path(__file__).parent / "assets" / "styles.css"
load_css(css_path)

# --- Sidebar (Logo + Info) ---
st.sidebar.image("assets/team9.png", width=140)
st.sidebar.markdown("<h3 style='text-align:center; color:#4CAF50;'>TEAM 9</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<hr>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align:center; color:#ccc;'>Innovating at the speed of creativity ⚡</p>", unsafe_allow_html=True)

# --- Page Controller ---
if "page" not in st.session_state:
    st.session_state.page = "home"

# --- PAGE 1: HOME ---
if st.session_state.page == "home":
    st.markdown("<div class='hero-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-title'>Hackathon Project</h1>", unsafe_allow_html=True)
    st.markdown("""
        <p class='description'>
        Welcome to <b>Team 9’s</b> hackathon innovation space 🚀<br>
        We combine AI, automation, and clean design to simplify problem solving.<br><br>
        Experience simplicity. Experience innovation.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("✨ Get Started ✨"):
        st.session_state.page = "upload"
        st.rerun()

# --- PAGE 2: UPLOAD PAGE ---
elif st.session_state.page == "upload":
    st.markdown("<h1 class='upload-title'>Upload & Analyze Your File</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Drop your files below 👇</p>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("", type=["csv", "txt", "xlsx"])

    if uploaded_file is not None:
        st.markdown("<div class='loading-text'>⏳ Analyzing file…</div>", unsafe_allow_html=True)
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.025)
            progress.progress(i + 1)
        st.markdown("<div class='loading-complete'>✅ Analysis complete!</div>", unsafe_allow_html=True)

        file_details = {
            "Filename": uploaded_file.name,
            "FileType": uploaded_file.type,
            "FileSize": f"{uploaded_file.size / 1024:.2f} KB"
        }
        st.json(file_details)

        st.markdown("<h3 class='output-title'>📊 Output</h3>", unsafe_allow_html=True)
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)
        elif uploaded_file.name.endswith(".txt"):
            content = uploaded_file.read().decode("utf-8")
            st.text_area("File Content:", content, height=300)
        else:
            st.info("📁 Preview not supported for this file type.")

    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
        st.rerun()
