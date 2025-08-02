# Home.py
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Smart Irrigation", layout="wide")

# --- Shared CSS Styling ---
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #e0f7fa, #e8f5e9);
        }
        section[data-testid="stSidebar"] {
            background-color: #b9f6ca;
        }
        .main-title {
            font-size: 38px;
            font-weight: bold;
            color: #1b5e20;
            text-align: left;
            margin-left: 20px;
        }
        .header-left {
            font-size: 26px;
            font-weight: bold;
            color: #004d40;
            padding-left: 10px;
        }
        .highlight-box {
            background-color: #dcedc8;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        }
        .note-text {
            font-style: italic;
            color: #2e7d32;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
col1, col2, col3 = st.columns([2, 5, 2])
with col1:
    st.markdown("<div class='header-left'>Mukilan</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<h1 class='main-title'>Smart Irrigation System</h1>", unsafe_allow_html=True)
with col3:
    edunet_logo = Image.open("assets/edunet_logo.png")
    aicte_logo = Image.open("assets/aicte_logo.png")
    col3a, col3b = st.columns(2)
    with col3a:
        st.image(edunet_logo, use_container_width=True)
    with col3b:
        st.image(aicte_logo, use_container_width=True)

# --- Content ---
left, right = st.columns([2, 1])
with left:
    st.markdown("<h3 style='color:#2e7d32;'>“Save Water – Every Drop Counts. Use Smart Farming Technology.”</h3>", unsafe_allow_html=True)

    st.markdown("<div class='highlight-box'>"
                "<h4>Why Smart Irrigation?</h4>"
                "<ul>"
                "<li>Reduces water waste by up to 50%</li>"
                "<li>Ensures optimal plant growth</li>"
                "<li>AI-based decision making for pump control</li>"
                "</ul>"
                "</div>", unsafe_allow_html=True)

    st.markdown("<p class='note-text'>✨ Our system continuously learns from your field’s sensor data to make smarter decisions every season!</p>", unsafe_allow_html=True)

with right:
    st.image("assets/field.png", use_container_width=True, caption="AI-powered field monitoring.")

st.markdown("---")
st.markdown("<center><p style='color:gray'>© 2025 Smart Irrigation by Mukilan K</p></center>", unsafe_allow_html=True)
