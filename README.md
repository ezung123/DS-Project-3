# 📊 Customer Churn Prediction Dashboard

A machine learning dashboard that predicts **telecom customer churn** using historical customer data.

The project demonstrates a complete **Data Science workflow**, from data preprocessing and model training to deployment using **Streamlit**.

---

## 🚀 Live Demo

👉 [https://your-streamlit-app-link](https://ds-project-3-2dvmkfjpxzgnu6tkvz9ulc.streamlit.app/)

---

## 🖥 Dashboard Preview

![Dashboard](dashboard.png)

---

## 📌 Problem Statement

Customer churn is a major issue for subscription-based businesses.

The goal of this project is to **predict whether a customer will churn**, allowing companies to take proactive actions such as:

- Offering discounts
- Improving service quality
- Providing personalized retention strategies

---

## 📊 Dataset

**Dataset:** Telco Customer Churn Dataset  
**Total Records:** 7043 customers  
**Target Variable:** `Churn` (Yes / No)

Feature categories include:

**Demographics**
- gender
- SeniorCitizen

**Account Information**
- tenure
- Contract

**Services**
- InternetService
- StreamingTV
- TechSupport

**Billing**
- MonthlyCharges
- TotalCharges
- PaymentMethod

---

## 🧠 Machine Learning Approach

### 1️⃣ Data Cleaning
- Converted `TotalCharges` to numeric
- Handled missing values
- Removed non-predictive column (`customerID`)

### 2️⃣ Data Preprocessing
- OneHotEncoding for categorical features
- StandardScaler for numeric features
- Implemented using a **Scikit-learn Pipeline**

### 3️⃣ Model Training
- Logistic Regression
- `class_weight='balanced'`
- Hyperparameter tuning with **GridSearchCV**

### 4️⃣ Model Evaluation
Metrics used:

- ROC-AUC
- Accuracy
- Recall (Churn class)

---

## 📈 Model Performance

| Metric | Score |
|------|------|
| ROC-AUC (Test) | ~0.86 |
| ROC-AUC (CV) | ~0.84 |
| Recall (Churn Class) | ~0.82 |
| Accuracy | ~0.75 |

The model prioritizes **recall for churn customers**, which is important for customer retention strategies.

---

## 📊 Dashboard Features

- 🔮 Customer churn prediction
- 📉 Churn probability gauge visualization
- 📊 Feature importance analysis
- 🧾 Business recommendations for retention

---

## 📂 Project Structure

```
DS-Project-3
│
├── app.py
├── churn_model.pkl
├── requirements.txt
│
└── pages
    ├── 1_Prediction.py
    ├── 2_Model_Insights.py
    └── 3_About.py
```

---

## ⚙️ Run Locally

Clone the repository:

```
git clone https://github.com/ezung123/DS-Project-3.git
cd DS-Project-3
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the Streamlit app:

```
streamlit run app.py
```

---

## 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Plotly
- Joblib

---

## 🔮 Future Improvements

- Add SHAP model explainability
- Experiment with advanced models (XGBoost, LightGBM)
- Implement automated threshold optimization
- Add customer segmentation analysis

---

## 👨‍💻 Author

Yan Ezung  
Computer Science Student | Aspiring Data Scientist