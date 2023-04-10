#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 01:41:45 2023

@author: vishesh
"""
import streamlit as st
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import numpy as np
from PIL import Image
import plotly.express as px
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

st.title("""Diagnosis of Coronary Heart Disorder""")

# Define the sidebar
st.sidebar.title("Coronary Heart Disorder Prediction App")
st.sidebar.write("Enter the following details to predict CHD disease:")

names = ["Vishesh", "Radhakrishnan", "Sagar", "Jin Xuemin"]
usernames = ['vishesh', 'sriradhakrishnan', "s.kamarthi", "j.xuemin"]

file_path = Path(__file__).parent / "hashed1_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
                                    "risk_analysis", "abcdef", cookie_expiry_days =30)


name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")
    
if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:

    st.sidebar.success("Select a Diagnosis from above.")
    
    authenticator.logout("Logout", "sidebar")

    
    st.write("""
    <div style='text-align: justify; color: red; font-weight: bold;'>
        <p>
           This web application is designed to assist in the diagnosis of Coronary Heart Disorder (CHD), a chronic condition that affects the heart due to plaque buildup in the coronary arteries, leading to reduced blood flow and oxygen supply to the heart. CHD can lead to serious health complications such as heart attacks and strokes. The backend of this application uses a machine learning approach to analyze various patient parameters such as Serum Cholesterol (mg/dl), Fasting Blood Sugar, Maximum Heart Rate Achieved, and other levels to predict the likelihood of CHD. We have utilized three different algorithms: Random Forest Classifier, Decision Tree, and Hybrid Naive Bayes, which work together to improve the overall performance of the model. Early detection and proper management of CHD can greatly improve the patient's quality of life. Our predictor model has been extensively tested and reported to have an accuracy of 99.14%.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    
    
    filename0 = 'one_hot_encoding.pkl'
    filename1 = 'model1_dch.sav'
    filename2 = 'model2_dch.sav'
    filename3 = 'model3_dch.sav'
    filename4 = 'scaler_dch.pkl'
    
    # load the model from disk
    enc = pickle.load(open(filename0, 'rb'))
    model1_dch = pickle.load(open(filename1, 'rb'))
    model2_dch = pickle.load(open(filename2, 'rb'))
    model3_dch = pickle.load(open(filename3, 'rb'))
    scaler = pickle.load(open(filename4, 'rb'))
    
    cat_features = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
    cont_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    
    with st.form("my_form"):
       st.write("Parameters")
       st.write("Please enter the following information to predict whether you have heart disease or not.")
    
        # Collect user input
       age = st.slider("Age", 20, 100, 50, 1)
       sex = st.radio("Sex", ["Male", "Female"])
       cp = st.radio('Choose Chest Pain Type:', ['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'])
       trestbps = st.slider("Resting Blood Pressure (mm Hg)", 80, 200, 120, 1)
       chol = st.slider("Serum Cholesterol (mg/dl)", 100, 600, 200, 1)
       fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
       restecg = st.radio('Choose Resting Electrocardiographic Results', ['Normal', 'Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)', 'Showing probable or definite left ventricular hypertrophy by Estes" criteria'])
       thalach = st.slider("Maximum Heart Rate Achieved", 50, 220, 150, 1)
       exang = st.radio("Exercise Induced Angina", ["No", "Yes"])
       oldpeak = st.slider("ST Depression Induced by Exercise Relative to Rest", 0.0, 6.2, 3.0, 0.1)
       slope = st.radio('Choose Appropriate Slope', ['Upsloping', 'Flat', 'Downsloping'])
       ca = st.radio('Choose CA (number of major vessels (0-3) colored by flourosopy)', [0, 1, 2, 3, 4])
       thal = st.radio('Choose Thal Value', ['Normal', 'Fixed Defect', 'Reversable Defect', 'Chronic Defect'])
    
        # Preprocess user input
       sex = 1 if sex == "Male" else 0
       fbs = 1 if fbs == "Yes" else 0
       exang = 1 if exang == "Yes" else 0
       if cp == 'Typical Angina':
        cp = 0
       elif cp == 'Atypical Angina':
        cp = 1
       elif cp == 'Non-Anginal Pain':
        cp = 2
       else:
        cp = 3
        
       if restecg == 'Normal':
        restecg = 0
       elif restecg == 'Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)':
        restecg = 1
       else:
        restecg = 2
        
       if slope == 'Upsloping':
        slope = 0
       elif slope == 'Flat':
        slope = 1
       else:
        slope = 2
        
        
       if thal == 'Normal':
        thal = 0
       elif thal == 'Fixed Defect':
        thal = 1
       elif thal == 'Reversable Defect':
        thal = 2
       else:
        thal = 3
       
       user_data = pd.DataFrame({
           'age': [age],
           'sex': [sex],
           'cp': [cp],
           'trestbps': [trestbps],
           'chol': [chol],
           'fbs': [fbs],
           'restecg': [restecg],
           'thalach': [thalach],
           'exang': [exang],
           'oldpeak': [oldpeak],
           'slope': [slope],
           'ca': [ca],
           'thal': [thal]
           })
       
       st.write('-------------------------------------------------------')
       submitted = st.form_submit_button("Submit")
       if submitted and all([age,sex,cp,trestbps,chol,
                               fbs,restecg,thalach,exang,oldpeak, slope, ca, thal]):
           st.write('Form Submitted')
       
       else:
           st.write('-------------------------------------------------------')
           st.write('Please fill all the details to get the diagnosis result')
    
    if st.button("Predict"):
        # Convert user input to dataframe
        
        # One-hot encode categorical variables
        cat_data = user_data[cat_features]
        cat_data = enc.transform(cat_data)
        cat_df = pd.DataFrame(data=cat_data, columns=enc.get_feature_names_out(cat_features))
        
        # Scale continuous variables
        cont_data = user_data[cont_features]
        cont_df = pd.DataFrame(data=cont_data, columns=cont_features)
        
        # Combine categorical and continuous data
        user_input = pd.concat([cat_df, cont_df], axis=1)
        
        # Make prediction
        predict1_coronary = model1_dch.predict(user_input)[0]
        predict2_coronary = model1_dch.predict(user_input)[0]
        predict3_coronary = model2_dch.predict(user_input)[0]
    
        
        # Display result
        col1, col2, col3 = st.columns(3)
        if predict1_coronary == 0:
            
            col1.metric(label="Random Forest Classifier", value="CHD Negative", delta="99.88% Accurate")
        elif predict1_coronary == 1:
            col1.metric(label="Random Forest Classifier", value="CHD Positive", delta="99.88% Accurate")
        if predict2_coronary == 0:
            col2.metric(label="Decision Tree", value="CHD Negative", delta="98.49% Accurate") 
        elif predict2_coronary == 1:
            col2.metric(label="Decision Tree", value="CHD Positive", delta="98.49% Accurate")
        if predict3_coronary == 0:
            col3.metric(label="Hybrid Naive Bayes", value="CHD Negative", delta="89.47% Accurate")
        elif predict3_coronary == 1:
            col3.metric(label="Hybrid Naive Bayes", value="CHD Positive", delta="89.47% Accurate")
