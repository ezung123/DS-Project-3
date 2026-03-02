# ============================================
# Streamlit App - Customer Churn Prediction
# ============================================

import streamlit as st
import pandas as pd
import joblib

# -------- Load Trained Model --------
model = joblib.load("churn_model.pkl")

st.set_page_config(page_title="Customer Churn Predictor", layout="wide")

st.title("📊 Customer Churn Prediction App")
st.write("Predict whether a customer is likely to churn based on account details.")

st.markdown("---")

# -------- Sidebar Inputs --------
st.sidebar.header("Enter Customer Details")

def user_input():

    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
    Partner = st.sidebar.selectbox("Has Partner", ["Yes", "No"])
    Dependents = st.sidebar.selectbox("Has Dependents", ["Yes", "No"])
    tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)

    PhoneService = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.sidebar.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    InternetService = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

    OnlineSecurity = st.sidebar.selectbox("Online Security", ["Yes", "No", "No internet service"])
    OnlineBackup = st.sidebar.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    DeviceProtection = st.sidebar.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    TechSupport = st.sidebar.selectbox("Tech Support", ["Yes", "No", "No internet service"])

    StreamingTV = st.sidebar.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    StreamingMovies = st.sidebar.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

    Contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.sidebar.selectbox(
        "Payment Method",
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
    )

    MonthlyCharges = st.sidebar.number_input("Monthly Charges", 0.0, 200.0, 70.0)
    TotalCharges = st.sidebar.number_input("Total Charges", 0.0, 10000.0, 1000.0)

    data = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    return pd.DataFrame([data])


input_df = user_input()

st.subheader("Customer Input Data")
st.write(input_df)

# -------- Prediction --------
if st.button("Predict Churn"):

    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[0][1]

    st.markdown("---")
    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error(f"⚠ Customer is likely to CHURN")
    else:
        st.success(f"✅ Customer is likely to STAY")

    st.write(f"Churn Probability: **{probability:.2f}**")

    # Risk Level Indicator
    if probability > 0.75:
        st.warning("🔴 High Risk Customer")
    elif probability > 0.5:
        st.info("🟡 Medium Risk Customer")
    else:
        st.success("🟢 Low Risk Customer")