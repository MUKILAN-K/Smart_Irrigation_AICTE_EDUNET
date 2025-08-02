# pages/predict.py
import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Prediction", layout="wide")

# --- Shared CSS Styling ---
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #f1f8e9, #e0f2f1);
        }
        section[data-testid="stSidebar"] {
            background-color: #b9f6ca;
        }
        .title {
            font-size: 35px;
            font-weight: bold;
            color: #388e3c;
            margin-bottom: 10px;
        }
        .subheader {
            font-size: 18px;
            color: #43a047;
            margin-bottom: 25px;
        }
        .result-on {
            color: #43a047;
            font-size: 20px;
        }
        .result-off {
            color: #e57373;
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Page Header ---
st.markdown('<div class="title">Smart Irrigation Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Enter sensor values (scaled 0 to 1):</div>', unsafe_allow_html=True)

# --- Load Model ---
model = joblib.load("model/Farm_Irrigation_System.pkl")

# --- Sensor Inputs in 4 Columns ---
sensor_values = []
cols = st.columns(4)
for i in range(20):
    with cols[i % 4]:
        val = st.slider(f"Sensor {i+1}", 0.0, 1.0, 0.5, 0.01)
        sensor_values.append(val)

# --- Prediction Output ---
if st.button("Predict"):
    prediction = model.predict([sensor_values])[0]

    st.markdown("### Prediction Result")
    st.markdown("---")

    for idx, status in enumerate(prediction):
        pump = f"P{idx+1}"
        if status == 1:
            st.markdown(f"<span class='result-on'>{pump} - ON ✅</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"<span class='result-off'>{pump} - OFF ❌</span>", unsafe_allow_html=True)
