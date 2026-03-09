import streamlit as st

st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction Dashboard")

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