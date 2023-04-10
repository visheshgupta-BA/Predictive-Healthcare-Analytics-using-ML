#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:27:19 2023

@author: vishesh
"""


import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import pickle
from pathlib import Path
import streamlit_authenticator as stauth



st.title("Diagnosis of Diabetes Mellitus")
st.sidebar.title("Diabetes Prediction App")
st.sidebar.write("Enter the following details to predict Diabetes:")

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
    <div style='text-align: justify; color: #bb33ff; font-weight: bold;'>
        <p>
            This web application is designed to assist in the diagnosis of diabetes mellitus, a chronic condition characterized by high blood sugar levels. Diabetes can lead to serious health complications such as heart disease, stroke, kidney disease, and nerve damage. The backend of this application uses a machine learning approach to enhance the performance of the model. We have utilized three different algorithms: XGBoost, Random Forest Classifier, and K-Nearest Neighbors. These algorithms work together to analyze various patient parameters such as age, BMI, blood pressure, and glucose levels to predict the likelihood of diabetes. Early detection and proper management of diabetes can greatly improve the patient's quality of life. Our predictor model has been extensively tested and reported.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    
    
    
    # Diabetes Mellitus Diagnosis Tool
    
    
    
    image = Image.open('/Users/vishesh/Documents/Major-Project-Deployment/black-image.jpeg')
    
    
    
    
    with st.form("my_form"):
        st.write("Parameters")
        
        
        Age = st.slider("Age", 15, 100, 50, 1)
        st.write('You Entered Age: %d' % int(Age))
        st.write('-------------------------------------------------------')
        
        Pregnancies = st.number_input('Enter your Number of Pregnancies')
        st.write('Your no. of Pregnancies %d' % int(Pregnancies))
        st.write('-------------------------------------------------------')
        
        Glucose = st.number_input('Glucose')
        st.write('You Entered Glucose is ', Glucose)
        st.write('-------------------------------------------------------')
    
        BloodPressure = st.number_input('BloodPressure')
        st.write('You Entered BloodPressure is ', BloodPressure)
        st.write('-------------------------------------------------------')
    
        Insulin = st.number_input('Insulin')
        st.write('You Entered Insulin is ', Insulin)
        st.write('-------------------------------------------------------')
    
        DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction')
        st.write('You Entered DiabetesPedigreeFunction is ', DiabetesPedigreeFunction)
        st.write('-------------------------------------------------------')
    
        SkinThickness = st.slider('SkinThickness', 0.0, 99.0, 0.1, 0.1)
        st.write("You Entered SkinThickness : ", SkinThickness)
        st.write('-------------------------------------------------------')
                
        BMI = st.slider('BMI', 0.0, 67.0, 0.1, 0.1)
        st.write("You Entered BMI : ", BMI)
    
        st.write('-------------------------------------------------------')
        submitted = st.form_submit_button("Submit")
        if submitted and all([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,
                               BMI,DiabetesPedigreeFunction,Age]):
            st.write('Form Submitted')
       
        else:
            st.write('-------------------------------------------------------')
            st.write('Please fill all the details to get the diagnosis result')
    
    
        
    df_diab = pd.DataFrame([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,
                            BMI,DiabetesPedigreeFunction,Age]], 
                          columns=['Pregnancies', 'Glucose', 'BloodPressure', 
                                   'SkinThickness', 'Insulin', 'BMI',
                                   'DiabetesPedigreeFunction', 'Age'])
    
    
    
    #st.table(df)
    #st.write("................................................................................................................................................................................")
    
    st.write("""
    #  Diagnosis Status :
    """)
    
    
    filename0 = 'scaler_db.pkl'
    scaler_db= pickle.load(open(filename0, 'rb'))
        
    df_diab_scaled = scaler_db.transform(df_diab)
    
    filename1 = 'model1_db.sav'
    filename2 = 'model2_db.sav'
    filename3 = 'model3_db.sav'
    
    # load the model from disk
    model1_db = pickle.load(open(filename1, 'rb'))
    model2_db = pickle.load(open(filename2, 'rb'))
    model3_db = pickle.load(open(filename3, 'rb'))
    
    predict1_db = model1_db.predict(df_diab_scaled)
    predict2_db = model2_db.predict(df_diab_scaled)
    predict3_db = model3_db.predict(df_diab_scaled)
    
    if st.button('Predict'):
        col1, col2, col3 = st.columns(3)
        if predict1_db == 1:
            col1.metric(label="XgBoost", value="Diabetic", delta="83.37% Accurate")
        elif predict1_db == 0:
            col1.metric(label="XgBoost", value="Non Diabetic", delta="83.37% Accurate")
        if predict2_db == 1:
            col2.metric(label="Random Forest", value="Diabetic", delta="82.31% Accurate") 
        elif predict2_db == 0: 
            col2.metric(label="Random Forest", value="Non Diabetic", delta="82.31% Accurate")
        if predict3_db == 1:
            col3.metric(label="K Nearest Classifier", value="Diabetic", delta="77.82% Accurate")
        elif predict3_db == 0:
            col3.metric(label="K Nearest Classifier", value="Non Diabetic", delta="77.82% Accurate")
