# ============================================
# Advanced Streamlit App - Customer Churn
# ============================================

import streamlit as st
import pandas as pd
import joblib

# -------- Page Config --------
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide"
)

# -------- Load Model --------
model = joblib.load("churn_model.pkl")


# -------- Function to Extract Feature Importance --------
def get_feature_importance(model):

    # Get classifier
    classifier = model.named_steps["classifier"]

    # Get preprocessing step
    preprocessor = model.named_steps["preprocessor"]

    # Get numeric and categorical feature names
    num_features = preprocessor.transformers_[0][2]
    cat_features = preprocessor.transformers_[1][1].get_feature_names_out(
        preprocessor.transformers_[1][2]
    )

    # Combine all feature names
    all_features = list(num_features) + list(cat_features)

    # Get coefficients
    coefficients = classifier.coef_[0]

    # Create dataframe
    feature_importance = pd.DataFrame({
        "Feature": all_features,
        "Coefficient": coefficients
    })

    return feature_importance.sort_values(by="Coefficient", ascending=False)


# -------- Business Recommendation Logic --------
def churn_recommendation(probability, contract, tenure):

    if probability > 0.75:
        return [
            "Offer a loyalty discount or promotional offer",
            "Encourage switching to a long-term contract",
            "Provide proactive customer support outreach"
        ]

    elif probability > 0.5:
        return [
            "Send engagement emails or service reminders",
            "Offer small upgrade incentives",
            "Monitor customer service interactions"
        ]

    else:
        return [
            "Customer is stable",
            "Maintain service quality",
            "Consider upselling premium services"
        ]


# -------- Title Section --------
st.title("📊 Customer Churn Prediction Dashboard")
st.markdown("Predict customer churn risk using a trained Machine Learning model.")
st.markdown("---")

# -------- Layout Columns --------
col1, col2 = st.columns([1, 1.2])

# ================= INPUT SECTION =================
with col1:
    st.header("📝 Customer Information")

    gender = st.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Has Partner", ["Yes", "No"])
    Dependents = st.selectbox("Has Dependents", ["Yes", "No"])
    tenure = st.slider("Tenure (Months)", 0, 72, 12)

    st.markdown("### 📡 Services")
    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

    st.markdown("### 💳 Billing")
    Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox(
        "Payment Method",
        ["Electronic check", "Mailed check",
         "Bank transfer (automatic)", "Credit card (automatic)"]
    )

    MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
    TotalCharges = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

    predict_button = st.button("🔍 Predict Churn Risk")

# ================= PREDICTION SECTION =================
with col2:
    st.header("📈 Prediction Result")

    if predict_button:

        input_data = pd.DataFrame([{
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
        }])

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        st.markdown("---")
        st.subheader("📊 Model Feature Importance")

        feature_df = get_feature_importance(model)

        top_positive = feature_df.head(5)
        top_negative = feature_df.tail(5)

        st.write("### 🔺 Top Features Increasing Churn Risk")
        st.bar_chart(top_positive.set_index("Feature")["Coefficient"])

        st.write("### 🔻 Top Features Decreasing Churn Risk")
        st.bar_chart(top_negative.set_index("Feature")["Coefficient"])

        st.markdown("### 🔢 Churn Probability")

        st.metric(
            label="Probability of Churn",
            value=f"{probability*100:.2f}%"
        )

        st.markdown("---")

        # Risk classification
        if probability > 0.75:
            st.error("🔴 High Risk Customer")
            st.write("Immediate retention strategy recommended.")
        elif probability > 0.5:
            st.warning("🟡 Medium Risk Customer")
            st.write("Monitor customer engagement.")
        else:
            st.success("🟢 Low Risk Customer")
            st.write("Customer likely to stay.")

    else:
        st.info("Enter customer details and click 'Predict Churn Risk'.")
    
    st.markdown("---")
    st.subheader("💡 Business Insight")

    recommendations = churn_recommendation(probability, Contract, tenure)

    for rec in recommendations:
        st.write(f"• {rec}")