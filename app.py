import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Gold Price Prediction",
    page_icon="💰",
    layout="centered"
)

# ------------------ LOAD MODEL ------------------
with open("goldloan.pkl", "rb") as f:
    model = pickle.load(f)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.main {
    background-color: #0f172a;
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #facc15;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #cbd5e1;
    margin-bottom: 30px;
}
.card {
    background: #020617;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0px 10px 30px rgba(250,204,21,0.15);
}
label {
    color: #e5e7eb !important;
}
.stButton>button {
    background: linear-gradient(90deg, #facc15, #eab308);
    color: black;
    font-weight: bold;
    border-radius: 10px;
    height: 50px;
    width: 100%;
}
.result {
    background: #022c22;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    color: #86efac;
    font-size: 22px;
    font-weight: bold;
}
.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 14px;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown('<div class="title">💰 Gold Price Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Machine Learning powered financial forecasting</div>', unsafe_allow_html=True)

# ------------------ INPUT CARD ------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    spx = st.number_input("📈 S&P 500 (SPX)", value=1400.0)
    uso = st.number_input("🛢️ Oil Price (USO)", value=75.0)
    eurusd = st.number_input("💱 EUR/USD", value=1.40)

with col2:
    slv = st.number_input("🥈 Silver Price (SLV)", value=15.0)
    year = st.number_input("📅 Year", min_value=2000, max_value=2035, value=2024)
    month = st.selectbox("🗓️ Month", list(range(1, 13)))

st.markdown("</div>", unsafe_allow_html=True)

# ------------------ PREDICTION ------------------
if st.button("🔮 Predict Gold Price"):
    input_data = np.array([[spx, uso, slv, eurusd]])
    prediction = model.predict(input_data)[0]


    st.markdown(
        f'<div class="result">Predicted Gold Price: ${prediction:.2f}</div>',
        unsafe_allow_html=True
    )

# ------------------ FOOTER ------------------
st.markdown(
    '<div class="footer">Built with ❤️ using Streamlit & Machine Learning</div>',
    unsafe_allow_html=True
)
