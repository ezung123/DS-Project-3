import streamlit as st
import joblib
import pandas as pd

model = joblib.load("churn_model.pkl")

st.title("📊 Model Insights")

classifier = model.named_steps["classifier"]
preprocessor = model.named_steps["preprocessor"]

num_features = preprocessor.transformers_[0][2]

cat_features = preprocessor.transformers_[1][1].get_feature_names_out(
    preprocessor.transformers_[1][2]
)

features = list(num_features) + list(cat_features)

coef = classifier.coef_[0]

df = pd.DataFrame({
    "Feature":features,
    "Coefficient":coef
})

df = df.sort_values(by="Coefficient",ascending=False)

st.bar_chart(df.head(10).set_index("Feature"))