import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/Churn.csv")

st.title("Dataset Explorer")

st.dataframe(df)

fig = px.histogram(df, x="Contract", color="Churn")

st.plotly_chart(fig)