#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:27:25 2023

@author: vishesh
"""
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
from PIL import Image
import pickle
from pathlib import Path
import streamlit_authenticator as stauth


st.title("Diagnosis of Heparus Liver Disease")
# Define the sidebar
st.sidebar.title("Liver Disease Prediction App")
st.sidebar.write("Enter the following details to predict liver disease:")

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

    st.write(
        """
        <div style="text-align: justify; color: #009933;">
           This web application predicts the likelihood of liver disease based on various patient features. Liver disease can be caused by a range of factors such as viruses, genetics, alcohol abuse, and obesity, and it can result in symptoms like fatigue, nausea, jaundice, and abdominal pain. Early detection and treatment of liver disease are crucial to prevent further liver damage. Our application uses an advanced machine learning model that analyzes patient data using algorithms such as Extra Tree Classifier, Random Forest Classifier, and Logistic Regression. Our model has been extensively tested and has shown high accuracy in diagnosing liver disease. Simply fill out the form below to get started.
        </div>
        <br>
        """,
        unsafe_allow_html=True
    )
    
    
    
    # Create the images
    image1 = Image.open('/Users/vishesh/Documents/Major-Project-Deployment/liver0.jpeg')
    image2 = Image.open('/Users/vishesh/Documents/Major-Project-Deployment/liver1.jpeg')
    image3 = Image.open('/Users/vishesh/Documents/Major-Project-Deployment/liver2.jpeg')
    
    # Create three columns in a container
    col1, col2, col3 = st.columns(3)
    
    # Add the images to each column
    with col1:
        resized_image1 = image1.resize((200, 200))
        st.image(resized_image1, caption="Chronic LD")
    
    with col2:
        st.image(image2, caption="Cirrhosis", width=200)
    
    with col3:
        st.image(image3, caption="Mubarhsis", width=200)
    
    

    
    with st.form("my_form"):
        st.write("Parameters")
    
        Age = st.slider("Age", 2, 100, 50, 1)
        st.write('Your Age %d' % int(Age))
    
    
        Gender = st.radio('Select your Gender', ['Male', 'Female'])
    
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                Total_Bilirubin = st.slider('Total Bilirubin', 0.0, 80.0, 14.0, 0.1)
    
                Direct_Bilirubin = st.slider('Direct Bilirubin', 0.1, 30.0, 14.0, 0.1)
    
                
                Alkaline_Phosphotase = st.number_input('Alkaline Phosphotase')
    
                
                Alamine_Aminotransferase = st.number_input('Alamine Aminotransferase')
                
    
            with col2:
                Aspartate_Aminotransferase = st.number_input('Aspartate Aminotransferase')
    
                Total_Protiens = st.slider('Total Proteins', 2.0, 11.0, 7.0, 0.1)
    
                Albumin = st.slider('Albumin', 0.0, 6.0, 3.0, 0.1)
    
                Albumin_and_Globulin_Ratio = st.slider('Albumin/Globulin Ratio', 0.0, 5.0, 2.5, 0.1)
        st.write('-------------------------------------------------------')
        submitted = st.form_submit_button("Submit")
        if submitted and all([Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase,
                              Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin,
                              Albumin_and_Globulin_Ratio]):
            st.write('Form Submitted')
    
        else:
            st.write('-------------------------------------------------------')
            st.write('Please fill all the details to get the diagnosis result')
    
    
    
    df_ld = pd.DataFrame([[Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,
                            Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin, Albumin_and_Globulin_Ratio]], 
                          columns=['Age', 'Gender', 'Total_Bilirubin', 'Direct_Bilirubin',
           'Alkaline_Phosphotase', 'Alamine_Aminotransferase',
           'Aspartate_Aminotransferase', 'Total_Protiens', 'Albumin',
           'Albumin_and_Globulin_Ratio'])
    
    df_ld['Gender'] = df_ld['Gender'].apply(lambda x: 1 if x=='Male' else 0)
    
    #st.table(df)
    #st.write("................................................................................................................................................................................")
    
    st.write("""
    #  Diagnosis Status :
    """)
    
    
    filename0 = 'scaler_ld.pkl'
    scaler= pickle.load(open(filename0, 'rb'))
        
    df_ld_scaled = scaler.transform(df_ld)
    
    filename1 = 'model1_ld.sav'
    filename2 = 'model2_ld.sav'
    filename3 = 'model3_ld.sav'
    
    # load the model from disk
    model1_ld = pickle.load(open(filename1, 'rb'))
    model2_ld = pickle.load(open(filename2, 'rb'))
    model3_ld = pickle.load(open(filename3, 'rb'))
    
    predict1_ld = model1_ld.predict(df_ld_scaled)
    predict2_ld = model2_ld.predict(df_ld_scaled)
    predict3_ld = model3_ld.predict(df_ld_scaled)
    
    if st.button('Predict'):
        col1, col2, col3 = st.columns(3)
        if predict1_ld == 1:
            col1.metric(label="Extra Tree Classifier", value="Heparus-Positive", delta="84.12% Accurate")
        elif predict1_ld == 2:
            col1.metric(label="Extra Tree Classifier", value="Heparus-Negative", delta="84.12% Accurate")
        if predict2_ld == 1:
            col2.metric(label="Random Forest Classifier", value="Heparus-Positive", delta="81.29% Accurate") 
        elif predict2_ld == 2:
            col2.metric(label="Random Forest Classifier", value="Heparus-Negative", delta="81.29% Accurate")
        if predict3_ld == 1:
            col3.metric(label="Logistic Regression", value="Heparus-Positive", delta="77.43% Accurate")
        elif predict3 == 2:
            col3.metric(label="Logistic Regression", value="Heparus-Negative", delta="77.43% Accurate")
