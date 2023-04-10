#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:30:13 2023

@author: vishesh
"""

import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import numpy as np
from pathlib import Path
import streamlit_authenticator as stauth


st.title("Risk Analysis Diagnosis DataBase")

st.sidebar.title("Risk Analysis DataBase App")
st.sidebar.write("Enter the following Dataframe to view Data Exploration and Relationship:")


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


    st.write("_______________________________________________________________________________________________________________________________________________")
    
    st.write("""
    ### Exploratory Data Analysis
    """)
    
    
    dataset = st.selectbox('Select a dataframe:', ('Breast Cancer', 'Sugar Diabetes', 'Kidney', 'Liver', 'Heart Disease'))
    
    # Load the appropriate dataset based on the user's choice
    if dataset == 'Breast Cancer':
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
        col_names = ['id', 'clump_thickness', 'uniform_cell_size', 'uniform_cell_shape',
           'marginal_adhesion', 'single_epithelial_size', 'bare_nuclei',
           'bland_chromatin', 'normal_nucleoli', 'mitoses', 'class']
    
        df_bcan = pd.read_csv(url, names=col_names)
        st.dataframe(df_bcan) 
        st.write("""
        ### Summary Statistics
        """)
        st.write(df_bcan.describe())
        st.write("_______________________________________________________________________________________________________________________________________________")
        
        fig1 = px.scatter(df_bcan, x='clump_thickness', y='uniform_cell_size', color='class',
        color_discrete_map={2: 'green', 4: 'red'},
        color_continuous_scale=['blue', 'red'],
        color_continuous_midpoint=3,
        labels={'clump_thickness': 'Clump thickness', 'uniform_cell_size': 'Uniform cell size'},
        title='Relationship of clump thickness vs. uniform cell size'
        )
        fig1.update_layout(title_x=0.22)
        fig1.update_traces(marker=dict(size=10))
        fig1.update_layout(coloraxis_colorbar=dict(title='Class', tickvals=[2, 4]))
        st.plotly_chart(fig1)
    
        
    elif dataset == 'Sugar Diabetes':
        df_sugar = pd.read_csv('/Users/vishesh/Documents/Major-Project-Deployment/sugar_diabetes.csv')
        st.dataframe(df_sugar) 
        st.write("""
        ### Summary Statistics
        """)
        st.write(df_sugar.describe())
        st.write("_______________________________________________________________________________________________________________________________________________")
    
        fig1 = px.histogram(df_sugar, x='Glucose', color='Outcome', nbins=20, opacity=0.8,
                        labels={'Glucose': 'Glucose level', 'Outcome': 'Diabetes status'},
                        title='Distribution of glucose levels for diabetic vs. non-diabetic patients')
        fig1.update_layout(title_x=0.16)
        fig1.update_layout(coloraxis_colorbar=dict(title='Outcome', tickvals=[1, 0]))
        st.plotly_chart(fig1)
    
    # Create scatter plot of insulin levels vs. BMI, colored by diabetes status
        fig2 = px.scatter(df_sugar, x='Insulin', y='BMI', color='Outcome',
                      color_discrete_map={0: 'green', 1: 'red'},
                      labels={'Insulin': 'Insulin level', 'BMI': 'Body mass index', 'Outcome': 'Diabetes status'},
                      title='Relationship Similarity of insulin levels vs. Body Mass Index')
        fig2.update_layout(title_x=0.19)
        fig2.update_layout(coloraxis_colorbar=dict(title='Outcome', tickvals=[1, 0]))
        st.plotly_chart(fig2)
        
    elif dataset == 'Kidney':
        df_kidney = pd.read_csv('/Users/vishesh/Documents/Major-Project-Deployment/kidney_disease.csv')
        st.dataframe(df_kidney)
        st.write("""
        ### Summary Statistics
        """)
        st.write(df_kidney.describe())
        
        fig = px.scatter(df_kidney, x='bp', y='sc', color='classification',
                     color_discrete_map={0: 'blue', 1: 'red'},
                     labels={'blood_pressure': 'Blood pressure', 'serum_creatinine': 'Serum creatinine'},
                     title='Scatter plot of blood pressure vs. serum creatinine, colored by target')
        fig.update_layout(title_x=0.18)
        st.plotly_chart(fig)
        
    elif dataset == 'Liver':
        df_liver = pd.read_csv('/Users/vishesh/Documents/Major-Project-Deployment/indian_liver_patient.csv')
        st.dataframe(df_liver)
        st.write("""
        ### Summary Statistics
        """)
        st.write(df_liver.describe())
        st.write("_______________________________________________________________________________________________________________________________________________")
        
        corr = df_liver.corr()
        sns.set(style='white')
    
        mask = np.zeros_like(corr)
        mask[np.triu_indices_from(mask)] = True
        fig, ax = plt.subplots(figsize=(10,10))
        heatmap = sns.heatmap(corr, annot=True, linewidths=0.5, mask=mask, cmap='coolwarm', square=True)
        heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':18}, pad=12)
        st.pyplot(fig)
        
        st.write("_______________________________________________________________________________________________________________________________________________")
    
        fig3 = px.scatter(df_liver, x='Total_Bilirubin', y='Direct_Bilirubin', color='Dataset',
                      color_discrete_sequence=['green', 'red'],
                      color_continuous_midpoint=3,
                      color_continuous_scale=['green', 'red'],
                      labels={'Total_Bilirubin': 'Total Bilirubin', 'Direct_Bilirubin': 'Direct Bilirubin',
                              'Dataset': 'Class'},
                      title='Relationship of Direct & Total bilirubin vs. serum creatinine differentiated by class')
        fig3.update_traces(marker=dict(size=7))
        fig3.update_layout(title_x=0.11)
        fig3.update_layout(coloraxis_colorbar=dict(title='Class', tickvals=[2, 4]))
        st.plotly_chart(fig3)
    
        
    else:
        df_chd = pd.read_csv('/Users/vishesh/Documents/Major-Project-Deployment/heart.csv')
        st.dataframe(df_chd)
        st.write("""
        ### Summary Statistics
        """)
        st.write(df_chd.describe())
        st.write("_______________________________________________________________________________________________________________________________________________")
       
        fig, ax = plt.subplots(figsize=(10,10))
        sns.heatmap(df_chd.corr(), annot=True, cmap='Blues', annot_kws={'fontsize': 12}, fmt='.2f', linewidths=0.5, ax=ax)
        ax.set_title('Correlation Between Features in Heart Disease Dataframe', fontsize=12)
        st.pyplot(fig)
    
        
        fig3 = px.scatter(df_chd, x='age', y='chol', color='target',
                      color_discrete_sequence=['green', 'red'],
                      color_continuous_scale=['blue', 'red'],
                      labels={'age': 'Age', 'chol': 'Cholesterol', 'target': 'Heart Disease'},
                      title='Relationship of Age and Cholesterol, Colored by Heart Disease')
        fig3.update_layout(coloraxis_colorbar=dict(title='target', tickvals=[1, 0]))
        fig3.update_layout(title_x=0.18)
        st.plotly_chart(fig3)
        