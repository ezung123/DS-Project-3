import streamlit as st

st.image("assets/dashboard_banner.png", use_container_width=True)

st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric(
    label="Total Customers",
    value="7043"
)

col2.metric(
    label="Churn Rate",
    value="26.5%"
)

col3.metric(
    label="Model ROC-AUC",
    value="0.86"
)

st.divider()

st.markdown("""
Welcome to the **Customer Churn Analytics Dashboard**.

This system predicts customer churn risk using a **Machine Learning model**.

### Features
- Customer churn prediction
- Risk visualization
- Model feature importance
- Dataset exploration

Use the sidebar to navigate.
""")