🏥 **Health Insurance Premium Prediction App**

📌 **Project Overview**

  This project is an end-to-end Machine Learning application that predicts health insurance premiums based on customer demographic, lifestyle, and medical information.
  
  The solution uses XGBoost regression models and is deployed using Streamlit, allowing users to interactively input details and instantly receive premium predictions.
  
  To improve accuracy, separate models are built for different age groups, as error analysis showed higher variance among younger customers.

🚀 **Features**

  Interactive Streamlit web application
  
  Predicts annual health insurance premium
  
  Handles both categorical and numerical features
  
  Separate ML models for:
  
  Customers ≤ 25 years
  
  Customers > 25 years
  
  Robust preprocessing:
  
  One-hot encoding
  
  Feature scaling
  
  Normalized medical risk score
  
  Error analysis to identify extreme prediction cases
  
  Ready for cloud deployment

📊 **Dataset Description**

  The model is trained on structured insurance data containing:
  
  Input Features
  
  Age
  
  Gender
  
  Region
  
  Marital Status
  
  Number of Dependants
  
  BMI Category
  
  Smoking Status
  
  Employment Status
  
  Income (Lakhs)
  
  Medical History
  
  Insurance Plan (Bronze / Silver / Gold)
  
  Genetical Risk Score
  
  Target Variable
  
  Annual Premium Amount

⚠️ Note: The original dataset is proprietary and cannot be shared publicly.

🤖 **Model Details**

**Algorithm**: XGBoost Regressor

  Hyperparameter Tuning: RandomizedSearchCV
  
  Evaluation Metric: R² Score
  
  Feature Engineering:
  
  Medical history converted into a normalized risk score
  
  Categorical features encoded
  
  Numerical features scaled
  
  Age-based Modeling Strategy
  Age Group	Model Used
  ≤ 25 years	model_young
  > 25 years	model_rest
  
  This approach significantly reduced extreme prediction errors.

📁 **Project Structure**
health-insurance-premium-prediction-app/

│

├── artifacts/

│   ├── premium_model_young.joblib

│   ├── premium_model_rest.joblib

│   ├── premium_scaler_young.joblib

│   └── premium_scaler_rest.joblib

│

├── main.py                 # Streamlit application

├── predict_helper.py       # Preprocessing & prediction logic

├── requirements.txt        # Project dependencies

├── README.md               # Project documentation

└── visuals/                # EDA & plots

🖥️ **How to Use the App**

  Open the Streamlit app in your browser through this URL : https://health-insurance-premium-prediction-app-6ddvctgdtvnxvhcjr5ehgz.streamlit.app/
  
  Enter customer details such as:
  
  Age
  
  Gender
  
  Income
  
  Medical History
  
  Insurance Plan
  
  Click Predict
  
  View the predicted insurance premium

📈 **Results & Insights**

Overall model accuracy is high (R² ≈ 0.98)

~30% of test cases had >10% prediction error initially

Majority of extreme errors came from age ≤ 25

Separate modeling reduced extreme errors to < 1% for older age group

