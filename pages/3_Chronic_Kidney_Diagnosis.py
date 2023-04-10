#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:27:23 2023

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


st.title("""Diagnosis of Chronic Kidney Disease""")

# Define the sidebar
st.sidebar.title("Chronic Kidney Prediction App")
st.sidebar.write("Enter the following details to predict Chronic Kidney Disease:")

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
        <div style="text-align: justify; color: #3366ff; font-weight: bold;">
            <p>
            This web application aims to improve the diagnosis of chronic kidney disease, a long-term medical condition that can lead to various health complications. By analyzing multiple patient parameters such as Specific Gravity Albumin, Blood Urea, and Serum Creatinine levels, our machine learning approach can predict the likelihood of kidney disease. To improve the overall performance of our model, we have utilized three different algorithms: Random Forest Classifier, Logistic Regression, and Gradient Boosting. Early detection and proper management of CKD can significantly enhance a patient's quality of life. Our predictor model has been rigorously tested and found to have an accuracy rate of 97.14%. By using this application, patients and healthcare providers can make informed decisions about managing this chronic condition. 
            </p>
        </div>
        <br>
    """, unsafe_allow_html=True)
    
    
    
    
    with st.form("my_form"):
        st.write("Parameters")
        
        age = st.slider("Age", 2, 100, 50, 1)
        st.write('You Entered Age: %d' % int(age))
        st.write('-------------------------------------------------------')
        
        blood_pressure = st.number_input('blood pressure')
        st.write('You Entered blood pressure is ', blood_pressure)
        st.write('-------------------------------------------------------')
    
        specific_gravity = st.number_input('Specific Gravity')
        st.write('You Entered Specific Gravity is ', specific_gravity)
        st.write('-------------------------------------------------------')
        
        albumin = st.number_input('Albumin')
        st.write('You Entered albumin is ', albumin)
        st.write('-------------------------------------------------------')
    
        sugar = st.number_input('Sugar')
        st.write('You Entered Sugar is ', sugar)
        st.write('-------------------------------------------------------')
           
        blood_glucose_random = st.number_input('Blood Glucose Random')
        st.write('You Entered blood pressure is ', blood_glucose_random)
        st.write('-------------------------------------------------------')
     
        blood_urea = st.number_input('Blood Urea')
        st.write('You Entered blood urea is ', blood_urea)
        st.write('-------------------------------------------------------')
           
        serum_creatinine = st.number_input('Serum Creatinine')
        st.write('You Entered Serum Creatinine is ', serum_creatinine)
        st.write('-------------------------------------------------------')    
        
        sodium = st.number_input('Sodium')
        st.write('You Entered Sodium is ', sodium)
        st.write('-------------------------------------------------------')
           
        potassium = st.number_input('Potassium')
        st.write('You Entered blood pressure is ', potassium)
        st.write('-------------------------------------------------------')
    
        haemoglobin = st.number_input('Haemoglobin')
        st.write('You Entered Haemoglobin is ', haemoglobin)
        st.write('-------------------------------------------------------')
           
        packed_cell_volume = st.number_input('Packed Cell Volume')
        st.write('You Entered Packed Cell Volume is ', packed_cell_volume)
        st.write('-------------------------------------------------------')
    
        white_blood_cell_count = st.number_input('White Blood Cell Count')
        st.write('You Entered White Blood Cell Count is ', white_blood_cell_count)
        st.write('-------------------------------------------------------')      
        
        red_blood_cell_count = st.number_input('Red Blood Cell Count')
        st.write('You Entered Red Blood Cell Count is ', red_blood_cell_count)
        st.write('-------------------------------------------------------')
        
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                red_blood_cells = st.radio('Select your Red Blood Cells', ['Normal', 'Abnormal'])
                pus_cell = st.radio('Select your Pus Cell', ['Normal', 'Abnormal'])
                pus_cell_clumps = st.radio('Select your Pus Cell Clumps', ['Present', 'Not Present'])
                bacteria = st.radio('Select your Bacteria', ['Present', 'Not Present'])
                hypertension = st.radio('Select your Hypertension', ['Yes', 'No'])
                   
    
            with col2: 
                diabetes_mellitus = st.radio('Select your Diabetes Mellitus', ['Yes', 'No'])
                coronary_artery_disease = st.radio('Select your Coronary Artery Disease', ['Yes', 'No'])
                peda_edema = st.radio('Select your Peda Edema', ['Yes', 'No'])
                aanemia = st.radio('Select your aanemia', ['Yes', 'No'])
                appetite = st.radio('Select your Appetite', ['Good', 'Poor'])
        st.write('-------------------------------------------------------')
                       
        
        submitted = st.form_submit_button("Submit")
        if submitted and all([age, blood_pressure, specific_gravity, albumin, sugar, blood_glucose_random,
                                   blood_urea, serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume,
                                   white_blood_cell_count, red_blood_cell_count, red_blood_cells, pus_cell, pus_cell_clumps, bacteria, hypertension, diabetes_mellitus,
                                                           coronary_artery_disease, appetite, peda_edema, aanemia]):
            st.write('Form Submitted')
           
        else:
            st.write('-------------------------------------------------------')
            st.write('Please fill all the details to get the diagnosis result')
        
        # result = loaded_model.score(X_test, Y_test)
        
        df_num = pd.DataFrame([[age, blood_pressure, specific_gravity, albumin, sugar, blood_glucose_random,
                                blood_urea, serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume,
                                white_blood_cell_count, red_blood_cell_count]], columns=['age', 'blood_pressure', 'specific_gravity', 'albumin', 'sugar',
                                                                                         'blood_glucose_random', 'blood_urea', 'serum_creatinine', 'sodium',
                                                                                         'potassium', 'haemoglobin', 'packed_cell_volume',
                                                                                         'white_blood_cell_count', 'red_blood_cell_count'])
                                                                                         
        
        df_cat = pd.DataFrame([[red_blood_cells, pus_cell, pus_cell_clumps, bacteria, hypertension, diabetes_mellitus,
                                coronary_artery_disease, appetite, peda_edema, aanemia]], columns=['red_blood_cells',
                                'pus_cell', 'pus_cell_clumps', 'bacteria', 'hypertension', 'diabetes_mellitus',
                                'coronary_artery_disease', 'appetite', 'peda_edema', 'aanemia'])
        
                                                                                                   
        df_cat['red_blood_cells'] = df_cat['red_blood_cells'].apply(lambda x: 1 if x=='Normal' else 0)
        df_cat['pus_cell'] = df_cat['pus_cell'].apply(lambda x: 1 if x=='Normal' else 0)
        df_cat['pus_cell_clumps'] = df_cat['pus_cell_clumps'].apply(lambda x: 1 if x=='Present' else 0)
        df_cat['bacteria'] = df_cat['bacteria'].apply(lambda x: 1 if x=='Present' else 0)
        df_cat['hypertension'] = df_cat['hypertension'].apply(lambda x: 1 if x=='Yes' else 0)
        df_cat['diabetes_mellitus'] = df_cat['diabetes_mellitus'].apply(lambda x: 1 if x=='Yes' else 0)
        df_cat['coronary_artery_disease'] = df_cat['coronary_artery_disease'].apply(lambda x: 1 if x=='Yes' else 0)
        df_cat['appetite'] = df_cat['appetite'].apply(lambda x: 1 if x=='Poor' else 0)
        df_cat['peda_edema'] = df_cat['peda_edema'].apply(lambda x: 1 if x=='Yes' else 0)
        df_cat['aanemia'] = df_cat['aanemia'].apply(lambda x: 1 if x=='Yes' else 0)
        
        
        #st.table(df)
        #st.write("................................................................................................................................................................................")
        
    st.write("""
        #  Diagnosis Status :
        """)
        
        
    filename0 = 'scaler_kd.pkl'
    scaler= pickle.load(open(filename0, 'rb'))
            
    df_scaled = scaler.transform(df_num)
        
    final_df = pd.DataFrame(data=df_scaled, columns = df_num.columns)
        
    concatenated_df = pd.concat([final_df, df_cat], axis=1)
        
    filename1 = 'model1_kd.sav'
    filename2 = 'model2_kd.sav'
    filename3 = 'model3_kd.sav'
        
        # load the model from disk
    model1_kd = pickle.load(open(filename1, 'rb'))
    model2_kd = pickle.load(open(filename2, 'rb'))
    model3_kd = pickle.load(open(filename3, 'rb'))
        
    predict1_kd = model1_kd.predict(concatenated_df)
    predict2_kd = model2_kd.predict(concatenated_df)
    predict3_kd = model3_kd.predict(concatenated_df)
        
    if st.button('Predict'):
        col1, col2, col3 = st.columns(3)
        if predict1_kd == 0:
            col1.metric(label="Random Forest Classifier", value="Glome..Negative", delta="97.50% Accurate")
        elif predict1_kd == 1:
            col1.metric(label="Random Forest Classifier", value="Glome..Positive", delta="97.50% Accurate")
        if predict2_kd == 0:
            col2.metric(label="Logistic Regression", value="Glome..Negative", delta="96.25% Accurate") 
        elif predict2_kd == 1:
            col2.metric(label="Logistic Regression", value="Glome..Positive", delta="96.25% Accurate")
        if predict3_kd == 0:
            col3.metric(label="Gradient Boosting", value="Glome..Negative", delta="96.34% Accurate")
        elif predict3_kd == 1:
            col3.metric(label="Gradient Boosting", value="Glome..Positive", delta="96.34% Accurate")
