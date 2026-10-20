import streamlit as st
import numpy as np
import pandas as pd
import joblib  # Fixed: Imported joblib instead of pickle

# Page configuration
st.set_page_config(
    page_title="Credit Card Fraud Detector",
    page_icon="💳",
    layout="centered"
)

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details below to evaluate the probability of a fraudulent transaction.")

# Load model directly from credit_card_model.pkl using joblib
@st.cache_resource
def load_model():
    try:
        # Fixed: Changed from pickle.load to joblib.load
        model = joblib.load('credit_card_model.pkl')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

if model is None:
    st.error("Model file (`credit_card_model.pkl`) not found or failed to load! Please check your file path.")
    st.stop()

# User Input Form
st.subheader("Transaction Features")

col1, col2 = st.columns(2)

with col1:
    time = st.number_input("Time (Seconds from first transaction)", min_value=0, value=10000)
    v1 = st.number_input("PCA Feature V1", value=0.0)
    v2 = st.number_input("PCA Feature V2", value=0.0)
    v3 = st.number_input("PCA Feature V3", value=0.0)

with col2:
    amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=150.0, step=10.0)
    # Provide default sliders or number inputs for others to satisfy the 30-feature model dimension
    st.info("Features V4-V28 will default to 0.0 for quick analysis.")

# Prediction Button
if st.button("Analyze Transaction Risk", type="primary"):
    # Construct the full 30-feature vector expected by the model:
    # ['Time', 'V1', 'V2', ..., 'V28', 'Amount']
    input_dict = {"Time": time, "V1": v1, "V2": v2, "V3": v3}
    
    # Default remaining PCA variables V4 to V28 to 0.0
    for i in range(4, 29):
        input_dict[f"V{i}"] = 0.0
        
    input_dict["Amount"] = amount
    
    # Convert to DataFrame to preserve feature names and strict column sequence
    input_df = pd.DataFrame([input_dict])
    
    # Predict directly using the loaded joblib model
    prediction = model.predict(input_df)[0]
    
    # Get probability if available
    if hasattr(model, "predict_proba"):
        fraud_probability = model.predict_proba(input_df)[0][1]
    else:
        fraud_probability = float(prediction)

    st.markdown("---")
    
    # Display Results
    if prediction == 1 or fraud_probability >= 0.5:
        st.error("🚨 **High Risk Warning:** Potential Fraud Detected!")
        st.metric(label="Fraud Risk Probability", value=f"{fraud_probability * 100:.2f}%")
    else:
        st.success("✅ **Transaction Safe:** Legitimate Activity Detected.")
        st.metric(label="Fraud Risk Probability", value=f"{fraud_probability * 100:.2f}%")