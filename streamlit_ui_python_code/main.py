import streamlit as st
from predict_helper import predict

st.title('Health Insurance Prediction App')

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}
col1, col2, col3 = st.columns(3)
# User Inputs
with col1:
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
    genetical_risk = st.number_input("Genetical Risk", min_value=0.0, max_value=10.0, step=1.0)
    gender = st.selectbox("Gender", ['Male', 'Female'])

    region = st.selectbox("Region",['Northwest', 'Southeast', 'Northeast', 'Southwest'])



with col2:


    number_of_dependants = st.number_input("Number of Dependants", min_value=0, max_value=10, step=1)

    bmi_category = st.selectbox("BMI Category",
                            ['Normal', 'Obesity', 'Overweight', 'Underweight'])

    smoking_status = st.selectbox("Smoking Status",
                              ['No Smoking', 'Regular', 'Occasional'])
    marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'])
with col3:

    employment_status = st.selectbox("Employment Status",
                                 ['Salaried', 'Self-Employed', 'Freelancer'])



    income_lakhs = st.number_input("Income in Lakhs", min_value=0.0, step=0.1)


    medical_history = st.selectbox("Medical History", [
        'Diabetes',
        'High blood pressure',
        'No Disease',
        'Diabetes & High blood pressure',
        'Thyroid',
        'Heart disease',
        'High blood pressure & Heart disease',
        'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ])

    insurance_plan = st.selectbox("Insurance Plan", ['Bronze', 'Silver', 'Gold'])

input_dict = {
    'Age': age,
    'Genetical Risk': genetical_risk,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Employment Status': employment_status,
    'Medical History': medical_history,
    'Insurance Plan': insurance_plan,
    'Number of Dependants': number_of_dependants,
    'Region': region,
    'Income in Lakhs': income_lakhs
}
if st.button("Predict"):
    prediction = predict(input_dict)
    st.success(f'Predicted Health Insurance Cost: {prediction}')