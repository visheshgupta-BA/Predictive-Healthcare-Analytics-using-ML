#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:27:30 2023

@author: vishesh
"""




import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import pickle
import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth


st.title("""Diagnosis of Breast Cancer""")

# Define the sidebar
st.sidebar.title("Breast Cancer Prediction App")
st.sidebar.write("Enter the following details to predict Breast Cancer:")

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
        <div style="text-align: justify; color: red; font-weight: bold;">
            <p>
            This is a web application that aids in the diagnosis of breast cancer by analyzing multiple parameters. The backend of this application uses a machine learning approach to enhance the performance of the model. We have utilized three different algorithms: Support Vector Machine, Random Forest Classifier, and K-Nearest Neighbors.These algorithms work together to analyze the input data and make predictions about the probability of breast cancer. The predictor model has been extensively tested, and the reported accuracy of the model is 96.14%
            </p>
        </div>
        <br>
    """, unsafe_allow_html=True)
    
    
    
    
    
    
    with st.form("my_form"):
       st.write("Parameters")
    
       clump_thickness = st.number_input('Clump thickness')
       st.write('You Entered Clump thickness: ', clump_thickness)
       st.write('-------------------------------------------------------')
    
       uniform_cell_size = st.number_input('Uniform Cell Size')
       st.write('You Entered Uniform Cell Size: ', uniform_cell_size)
       st.write('-------------------------------------------------------')
    
       uniform_cell_shape = st.number_input('Uniform Cell Shape')
       st.write('You Entered Uniform Cell Shape: ', uniform_cell_shape)
       st.write('-------------------------------------------------------')
    
       marginal_adhesion = st.number_input('Marginal Adhesion')
       st.write('You Entered Marginal Adhesion: ', marginal_adhesion)
       st.write('-------------------------------------------------------')
       
    
       single_epithelial_size = st.number_input('Single Epithelial Size')
       st.write('You Entered Single Epithelial Size: ', single_epithelial_size)
       st.write('-------------------------------------------------------')
    
       bare_nuclei = st.number_input('Bare Nuclei')
       st.write('You Entered Bare Nuclei: ', bare_nuclei)
       st.write('-------------------------------------------------------')
    
       bland_chromatin = st.number_input('Bland Chromatin')
       st.write('You Entered Bland Chromatin: ', bland_chromatin)
       st.write('-------------------------------------------------------')
    
       normal_nucleoli = st.number_input('Normal Nucleoli')
       st.write('You Entered Normal Nucleoli: ', normal_nucleoli)
       st.write('-------------------------------------------------------')
    
       mitoses = st.number_input('Mitoses')
       st.write('You Entered Mitoses: ', mitoses)
       st.write('-------------------------------------------------------')
       
       submitted = st.form_submit_button("Submit")
       if submitted and all([clump_thickness,uniform_cell_size,uniform_cell_shape,marginal_adhesion,single_epithelial_size,
                               bare_nuclei,bland_chromatin,normal_nucleoli,mitoses]):
           st.write('Form Submitted')
       
       else:
           st.write('-------------------------------------------------------')
           st.write('Please fill all the details to get the diagnosis result')
    
    # result = loaded_model.score(X_test, Y_test)
        
    
    
    df = pd.DataFrame([[clump_thickness,uniform_cell_size,uniform_cell_shape,marginal_adhesion,single_epithelial_size,
                            bare_nuclei,bland_chromatin,normal_nucleoli,mitoses]], 
                          columns=['clump_thickness', 'uniform_cell_size', 'uniform_cell_shape', 
                                   'marginal_adhesion', 'single_epithelial_size', 'bare_nuclei',
                                   'bland_chromatin', 'normal_nucleoli', 'mitoses'])
    
    
    
    #st.table(df)
    #st.write("................................................................................................................................................................................")
    
    st.write("""
    #  Diagnosis Status :
    """)
    
    
    filename0 = 'scaler_bc.pkl'
    scaler= pickle.load(open(filename0, 'rb'))
        
    df_scaled = scaler.transform(df)
    
    filename1 = 'model1_bc.sav'
    filename2 = 'model2_bc.sav'
    filename3 = 'model3_bc.sav'
    
    # load the model from disk
    model1 = pickle.load(open(filename1, 'rb'))
    model2 = pickle.load(open(filename2, 'rb'))
    model3 = pickle.load(open(filename3, 'rb'))
    
    predict1 = model1.predict(df_scaled)
    predict2 = model2.predict(df_scaled)
    predict3 = model3.predict(df_scaled)
    
    if st.button('Predict'):
        col1, col2, col3 = st.columns(3)
        if predict1 == 2:
            col1.metric(label="SVM", value="Benign", delta="97.85% Accurate")
        elif predict1 == 4:
            col1.metric(label="SVM", value="Malignant", delta="97.85% Accurate")
        if predict2 == 2:
            col2.metric(label="Random Forest Classifier", value="Benign", delta="97.42% Accurate") 
        elif predict2 == 4:
            col2.metric(label="Random Forest Classifier", value="Malignant", delta="97.42% Accurate")
        if predict3 == 2:
            col3.metric(label="K Nearest Classifier", value="Benign", delta="96.14% Accurate")
        elif predict3 == 4:
            col3.metric(label="K Nearest Classifier", value="Malignant", delta="96.14% Accurate")
    
