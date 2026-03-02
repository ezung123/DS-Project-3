# Customer Churn Prediction (Machine Learning Project)

## 📌 Problem Statement
Customer churn is a major issue for subscription-based businesses. 
The goal of this project is to build a machine learning model that predicts whether a customer is likely to churn.

By identifying at-risk customers, companies can take preventive actions such as offering discounts or improving services.

---

## 📊 Dataset
- Dataset: Telco Customer Churn Dataset
- Total Records: 7043 customers
- Target Variable: `Churn` (Yes / No)

Features include:
- Demographics (gender, SeniorCitizen)
- Account information (tenure, Contract)
- Service usage (InternetService, StreamingTV)
- Billing information (MonthlyCharges, TotalCharges)

---

## 🧠 Approach

1. Data Cleaning
   - Converted TotalCharges to numeric
   - Handled missing values
   - Dropped non-predictive column (customerID)

2. Preprocessing
   - OneHotEncoding for categorical variables
   - StandardScaler for numeric features

3. Model
   - Logistic Regression with class_weight='balanced'
   - Hyperparameter tuning using GridSearchCV
   - Evaluation using ROC-AUC

---

## 📈 Model Performance

- Best CV ROC-AUC: ~0.84
- Test ROC-AUC: ~0.86
- Recall (Churn Class): ~0.82
- Accuracy: ~0.75

The model performs well in identifying churn customers, which is critical for business retention strategies.

---
## 🚀 How to Run This Project

1. Clone the repository:

git clone <your-repository-link>

2. Navigate into the project folder:

cd DS-Project-3

3. Install required packages:

pip install -r requirements.txt

4. Run the project:

python main.py


---

## 🛠 Technologies Used

- Python
- pandas
- scikit-learn
- matplotlib
- joblib

---

## 🔮 Future Improvements

- Deploy model using Streamlit
- Add SHAP explainability
- Try advanced models (XGBoost, LightGBM)
- Automate threshold optimization

---

## 👨‍💻 Author
Yan Ezung
