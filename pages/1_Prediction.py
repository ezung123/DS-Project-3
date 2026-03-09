import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

model = joblib.load("churn_model.pkl")

st.title("🔮 Predict Customer Churn")

# CUSTOMER INFO
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0,1])
Partner = st.selectbox("Partner", ["Yes","No"])
Dependents = st.selectbox("Dependents", ["Yes","No"])
tenure = st.slider("Tenure",0,72,12)

# PHONE SERVICES
PhoneService = st.selectbox("Phone Service",["Yes","No"])
MultipleLines = st.selectbox(
    "Multiple Lines",
    ["No","Yes","No phone service"]
)

# INTERNET SERVICES
InternetService = st.selectbox(
    "Internet Service",
    ["DSL","Fiber optic","No"]
)

OnlineSecurity = st.selectbox(
    "Online Security",
    ["Yes","No","No internet service"]
)

OnlineBackup = st.selectbox(
    "Online Backup",
    ["Yes","No","No internet service"]
)

DeviceProtection = st.selectbox(
    "Device Protection",
    ["Yes","No","No internet service"]
)

TechSupport = st.selectbox(
    "Tech Support",
    ["Yes","No","No internet service"]
)

StreamingTV = st.selectbox(
    "Streaming TV",
    ["Yes","No","No internet service"]
)

StreamingMovies = st.selectbox(
    "Streaming Movies",
    ["Yes","No","No internet service"]
)

# BILLING
Contract = st.selectbox(
    "Contract",
    ["Month-to-month","One year","Two year"]
)

PaperlessBilling = st.selectbox(
    "Paperless Billing",
    ["Yes","No"]
)

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

MonthlyCharges = st.number_input(
    "Monthly Charges",
    0.0,200.0,70.0
)

TotalCharges = st.number_input(
    "Total Charges",
    0.0,10000.0,1000.0
)

if st.button("Predict Churn"):

    input_data = pd.DataFrame({
        "gender":[gender],
        "SeniorCitizen":[SeniorCitizen],
        "Partner":[Partner],
        "Dependents":[Dependents],
        "tenure":[tenure],
        "PhoneService":[PhoneService],
        "MultipleLines":[MultipleLines],
        "InternetService":[InternetService],
        "OnlineSecurity":[OnlineSecurity],
        "OnlineBackup":[OnlineBackup],
        "DeviceProtection":[DeviceProtection],
        "TechSupport":[TechSupport],
        "StreamingTV":[StreamingTV],
        "StreamingMovies":[StreamingMovies],
        "Contract":[Contract],
        "PaperlessBilling":[PaperlessBilling],
        "PaymentMethod":[PaymentMethod],
        "MonthlyCharges":[MonthlyCharges],
        "TotalCharges":[TotalCharges]
    })

    probability = model.predict_proba(input_data)[0][1]

    # Determine risk category
    if probability > 0.7:
        risk = "High Risk 🔴"
    elif probability > 0.4:
        risk = "Medium Risk 🟡"
    else:
        risk = "Low Risk 🟢"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability*100,
        title={'text':"Churn Risk (%)"},
        gauge={
            'axis':{'range':[0,100]},
            'steps':[
                {'range':[0,40],'color':'lightgreen'},
                {'range':[40,70],'color':'khaki'},
                {'range':[70,100],'color':'salmon'}
            ]
        }
    ))

    st.plotly_chart(fig)

    st.subheader("Customer Risk Level")

    st.markdown(f"## {risk}")

    st.write(f"### Churn Probability: {probability:.2%}")

    if probability > 0.7:
        st.warning("Recommended Action: Offer loyalty discount or contract upgrade")

    elif probability > 0.4:
        st.info("Recommended Action: Increase engagement through promotional offers")

    else:
        st.success("Customer is stable. Opportunity for upselling premium services")