import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('attrition_model.pkl')

# Streamlit UI
st.set_page_config(page_title="Employee Attrition Prediction", layout="centered")
st.title("Employee Attrition Prediction App")
st.markdown("Predict whether an employee will leave the company based on provided information.")

# Collect inputs
age = st.number_input('Age', min_value=18, max_value=65, value=30)
years_at_company = st.number_input('Years at Company', min_value=0, max_value=40, value=5)
monthly_income = st.number_input('Monthly Income (USD)', min_value=1000, max_value=50000, value=5000)
distance_from_home = st.number_input('Distance from Home (km)', min_value=0, max_value=100, value=10)
job_satisfaction = st.slider('Job Satisfaction (1=Low, 4=High)', 1, 4, 3)
work_life_balance = st.slider('Work Life Balance (1=Bad, 4=Excellent)', 1, 4, 3)
overtime = st.selectbox('OverTime', ['Yes', 'No'])  # keep as string if trained that way

# Prepare input data exactly as in training
input_data = pd.DataFrame({
    'Age': [age],
    'YearsAtCompany': [years_at_company],
    'MonthlyIncome': [monthly_income],
    'DistanceFromHome': [distance_from_home],
    'JobSatisfaction': [job_satisfaction],
    'WorkLifeBalance': [work_life_balance],
    'OverTime': [overtime]  # keep as 'Yes' or 'No' if training used that
})

# Predict
if st.button('Predict Attrition'):
    try:
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            st.error('This employee is likely to leave the company.')
        else:
            st.success('This employee is likely to stay with the company.')
    except Exception as e:
        st.error(f"Prediction failed. Error: {e}")
['Age', 'YearsAtCompany', 'MonthlyIncome', 'DistanceFromHome',
 'JobSatisfaction', 'WorkLifeBalance', 'OverTime']

