import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("Linear_Regression_Batch_2.pkl")

# Page settings
st.set_page_config(
    page_title="Gold Price Prediction",
    page_icon="🥇",
    layout="centered"
)

# Title
st.title("🥇 Gold Price Prediction")
st.write("Predict the Gold Close Price using Open, High, Low values.")

st.markdown("---")

# Input fields
open_price = st.number_input("Open Price", min_value=0.0, format="%.2f")
high_price = st.number_input("High Price", min_value=0.0, format="%.2f")
low_price = st.number_input("Low Price", min_value=0.0, format="%.2f")

# Predict button
if st.button("Predict"):

    input_data = np.array([[open_price, high_price, low_price]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Close Price: ${prediction.item():.2f}")