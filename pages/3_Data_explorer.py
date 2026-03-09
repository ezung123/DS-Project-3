import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Data Explorer")

# Load dataset
df = pd.read_csv("data/churn.csv")

st.subheader("Dataset Preview")
st.dataframe(df)

# -------------------------------
# Churn Distribution
# -------------------------------

st.subheader("Churn Distribution")

fig1 = px.pie(
    df,
    names="Churn",
    title="Customer Churn Distribution"
)

st.plotly_chart(fig1, use_container_width=True, key="pie_churn")


# -------------------------------
# Contract vs Churn
# -------------------------------

st.subheader("Contract Type vs Churn")

fig2 = px.histogram(
    df,
    x="Contract",
    color="Churn",
    barmode="group"
)

st.plotly_chart(fig2, use_container_width=True, key="contract_churn")


# -------------------------------
# Monthly Charges vs Churn
# -------------------------------

st.subheader("Monthly Charges vs Churn")

fig3 = px.box(
    df,
    x="Churn",
    y="MonthlyCharges"
)

st.plotly_chart(fig3, use_container_width=True, key="charges_churn")


# -------------------------------
# Tenure vs Churn
# -------------------------------

st.subheader("Tenure vs Churn")

fig4 = px.box(
    df,
    x="Churn",
    y="tenure"
)

st.plotly_chart(fig4, use_container_width=True, key="tenure_churn")