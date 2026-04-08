import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open('ebill_prediction_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>⚡ Electricity Bill Predictor</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center;'>Let's estimate your electricity bill based on your daily lifestyle </p>", unsafe_allow_html=True)

st.markdown("---")


col1, col2 = st.columns(2)

with col1:
    num_rooms = st.number_input("How many rooms do you have?", 1, 10)
    num_people = st.number_input("How many people live in your home?", 1, 10)
    housearea = st.number_input("What is the approximate house area?")
    
with col2:
    num_children = st.number_input("Number of children", 0, 5)
    is_urban = st.selectbox("Do you live in an urban area?", ["No", "Yes"])

st.markdown("---")

# Section Heading
st.markdown("### ⚡ Appliance usage")

col3, col4 = st.columns(2)

with col3:
    is_ac = st.selectbox("Do you use an AC?", ["No", "Yes"])
    is_tv = st.selectbox("Do you use a TV?", ["No", "Yes"])

with col4:
    is_flat = st.selectbox("Do you live in a flat?", ["No", "Yes"])

# Convert categorical to numeric
is_ac = 1 if is_ac == "Yes" else 0
is_tv = 1 if is_tv == "Yes" else 0
is_flat = 1 if is_flat == "Yes" else 0
is_urban = 1 if is_urban == "Yes" else 0

st.markdown("---")

# Button
predict_btn = st.button("✨ Estimate My Bill")

# Prediction
if predict_btn:
    data = np.array([[num_rooms, num_people, housearea, is_ac, is_tv,is_flat, num_children, is_urban]])

    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)

    st.markdown(
        f"<h2 style='text-align:center; color:#2e7d32;'>💰 Your estimated electricity bill is ₹{prediction[0]:.2f}</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;'>This is an approximate value based on your inputs.</p>",
        unsafe_allow_html=True
    )