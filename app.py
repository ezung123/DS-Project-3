# ================= IMPORT LIBRARIES =================
import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go


# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Customer Churn Prediction Dashboard",
    page_icon="📊",
    layout="wide"
)


# ================= LOAD TRAINED MODEL =================
model = joblib.load("churn_model.pkl")

# ================= FEATURE IMPORTANCE FUNCTION =================
def get_feature_importance(model):

    classifier = model.named_steps["classifier"]
    preprocessor = model.named_steps["preprocessor"]

    num_features = preprocessor.transformers_[0][2]

    cat_features = preprocessor.transformers_[1][1].get_feature_names_out(
        preprocessor.transformers_[1][2]
    )

    all_features = list(num_features) + list(cat_features)

    coefficients = classifier.coef_[0]

    feature_importance = pd.DataFrame({
        "Feature": all_features,
        "Coefficient": coefficients
    })

    return feature_importance.sort_values(by="Coefficient", ascending=False)

# ================= BUSINESS RECOMMENDATION FUNCTION =================
def churn_recommendation(probability, contract, tenure):

    if probability > 0.75:
        return [
            "Offer loyalty discount to retain customer",
            "Encourage switching to a long-term contract",
            "Provide proactive customer support"
        ]

    elif probability > 0.5:
        return [
            "Send engagement emails",
            "Offer service upgrade incentives",
            "Monitor customer usage patterns"
        ]

    else:
        return [
            "Customer is stable",
            "Maintain service quality",
            "Consider upselling premium services"
        ]
    
# ================= GAUGE CHART FUNCTION =================
def create_gauge(probability):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability * 100,
        title={'text': "Churn Risk (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'steps': [
                {'range': [0, 40], 'color': "lightgreen"},
                {'range': [40, 70], 'color': "khaki"},
                {'range': [70, 100], 'color': "salmon"}
            ]
        }
    ))

    return fig

# ================= GAUGE CHART FUNCTION =================
def create_gauge(probability):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability * 100,
        title={'text': "Churn Risk (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'steps': [
                {'range': [0, 40], 'color': "lightgreen"},
                {'range': [40, 70], 'color': "khaki"},
                {'range': [70, 100], 'color': "salmon"}
            ]
        }
    ))

    return fig

# ================= HOME PAGE =================
if page == "Home":

    st.title("📊 Customer Churn Prediction Dashboard")

    st.markdown("""
    This application predicts whether a telecom customer is likely to churn using a trained machine learning model.

    ### Features of this Dashboard
    - Predict customer churn probability
    - Visualize churn risk
    - Business recommendations for retention
    - Model feature importance insights

    Use the **Prediction page** from the sidebar to test the model.
    """)

# ================= PREDICTION PAGE =================
if page == "Prediction":

    col1, col2 = st.columns([1, 1.2])

    # INPUT COLUMN
    with col1:

        st.header("📝 Customer Information")

        gender = st.selectbox("Gender", ["Male", "Female"])
        SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
        Partner = st.selectbox("Has Partner", ["Yes", "No"])
        Dependents = st.selectbox("Has Dependents", ["Yes", "No"])
        tenure = st.slider("Tenure (Months)", 0, 72, 12)

        st.markdown("### 💳 Billing")

        Contract = st.selectbox(
            "Contract Type",
            ["Month-to-month", "One year", "Two year"]
        )

        MonthlyCharges = st.number_input(
            "Monthly Charges",
            0.0,
            200.0,
            70.0
        )

        TotalCharges = st.number_input(
            "Total Charges",
            0.0,
            10000.0,
            1000.0
        )

        predict_button = st.button("Predict Churn Risk")

# ================= PREDICTION PAGE =================
if page == "Prediction":

    col1, col2 = st.columns([1, 1.2])

    # INPUT COLUMN
    with col1:

        st.header("📝 Customer Information")

        gender = st.selectbox("Gender", ["Male", "Female"])
        SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
        Partner = st.selectbox("Has Partner", ["Yes", "No"])
        Dependents = st.selectbox("Has Dependents", ["Yes", "No"])
        tenure = st.slider("Tenure (Months)", 0, 72, 12)

        st.markdown("### 💳 Billing")

        Contract = st.selectbox(
            "Contract Type",
            ["Month-to-month", "One year", "Two year"]
        )

        MonthlyCharges = st.number_input(
            "Monthly Charges",
            0.0,
            200.0,
            70.0
        )

        TotalCharges = st.number_input(
            "Total Charges",
            0.0,
            10000.0,
            1000.0
        )

        predict_button = st.button("Predict Churn Risk")

# ================= MODEL INSIGHTS PAGE =================
if page == "Model Insights":

    st.title("📊 Model Insights")

    feature_df = get_feature_importance(model)

    st.subheader("Top Features Increasing Churn Risk")

    st.bar_chart(
        feature_df.head(10).set_index("Feature")["Coefficient"]
    )

    st.subheader("Top Features Decreasing Churn Risk")

    st.bar_chart(
        feature_df.tail(10).set_index("Feature")["Coefficient"]
    )

# ================= ABOUT PAGE =================
if page == "About":

    st.title("ℹ About This Project")

    st.markdown("""
    ### Customer Churn Prediction Project

    This project demonstrates a complete machine learning workflow including:

    - Data preprocessing
    - Model training
    - Hyperparameter tuning
    - Model evaluation
    - Web application deployment

    ### Technologies Used
    - Python
    - Pandas
    - Scikit-learn
    - Streamlit
    - Plotly

    ### Author
    Yan Ezung
    """)


    
