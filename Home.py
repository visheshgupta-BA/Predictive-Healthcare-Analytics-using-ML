#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:37:37 2023

@author: vishesh
"""


import streamlit as st
import pickle
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit_authenticator as stauth


st.set_page_config(
    page_title="Vishesh Diagnostic & Research Labs",
    page_icon="microscope",
)

# Define the sidebar layout
st.sidebar.write("Contact us:")
st.sidebar.write("- Phone: <a href='tel:[8573130666]'><i class='fas fa-phone'></i> [8573130666]</a>", unsafe_allow_html=True)
st.sidebar.write("- Email: <a href='mailto:[gupta.vishe@northeastern.edu]'><i class='far fa-envelope'></i> [gupta.vishe@northeastern.edu]</a>", unsafe_allow_html=True)
st.sidebar.write("- GitHub: <a href='https://github.com/visheshgupta-BA/' target='_blank'><i class='fab fa-github'></i> Vishesh Gupta's GitHub</a>", unsafe_allow_html=True)
st.sidebar.write("- Website: <a href='https://visheshgupta-ba.github.io/VisheshGupta/' target='_blank'><i class='fas fa-globe'></i> Vishesh Gupta's website</a>", unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color: #e6005c;'>Vishesh Diagnostic & Research Labs</h1>", unsafe_allow_html=True)

st.write("<p style='font-size: medium;'>@ Created by Vishesh Gupta</p>", unsafe_allow_html=True)

st.write("""
        <div style="text-align: justify; color: #1a1aff; font-weight: bold;">
            <p>
            Vishesh Diagnostics and Research labs began its operations in 2023 from Northeastern University, Boston, and has become a pioneer in the field of Health, Data, and Machine Learning. The journey began with a lab and predictions of diagnosis, and has today reached a stage where VDRL is in the top league in terms of the range and quality of diagnostic facilities, with the capability to perform more than 100 tests in-house. Vishesh Diagnostic & Research Centre offers a complete range of diagnostic facilities.
            </p>
        </div>
        <br>
    """, unsafe_allow_html=True)


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
    st.markdown("<p style='text-align: justify; color: #1a1aff; font-weight: normal;'>- To learn more about founder of VDRL in detail, click on this link: <a href='https://visheshgupta-ba.github.io/VisheshGupta/' style='color: red;'>https://visheshgupta-ba.github.io/VisheshGupta/</a></p>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: justify; color: #1a1aff; font-weight: normal;'>- To provide accurate and efficient healthcare services, we specialize in diagnosing 5 healthcare issues: Breast cancer, diabetes, coronary heart disorder, liver disease, and kidney disease. These diseases are briefly described below:</p>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: justify; color: #1a1aff; font-weight: normal;'>- Breast cancer: A type of cancer that starts in the cells of the breast. It is the most common cancer among women.</p>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: justify; color: #1a1aff; font-weight: normal;'>- Diabetes: A chronic condition that affects the way your body processes blood sugar (glucose).</p>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: justify; color: #1a1aff; font-weight: normal;'>- Coronary heart disorder: A disease that affects the arteries that supply blood to the heart muscle. It is usually caused by a buildup of plaque in the arteries.</p>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: justify; color: #1a1aff; font-weight: normal;'>- Liver disease: A condition that affects the liver's ability to function properly. It can be caused by viruses, alcohol use, or obesity.</p>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: justify; color: #1a1aff; font-weight: normal;'>- Kidney disease: A condition in which the kidneys do not function properly. It can be caused by diabetes, high blood pressure, or other factors.</p>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: justify; color: #1a1aff; font-weight: normal;'>- Our diagnoses are based on predictions made using machine learning algorithms. We use several different models to predict each diagnosis.</p>", unsafe_allow_html=True)
    
    # Add some more text and images to showcase your lab's services and facilities
    st.write('-------------------------------------------------------')
    
    st.markdown("<h2 style='color: #ff4d94;'>Our Services</h2>", unsafe_allow_html=True)
    st.write("At Vishesh Gupta's Diagnosis Labs, we offer a wide range of diagnostic services, including:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("S-0.jpeg", width=200)
        st.write("<p style='text-align: center; color: #00b33c;'>Breast Cancer Diagnosis</p>", unsafe_allow_html=True)
    
    with col2:
        st.image("s-1.jpeg", width=200)
        st.write("<p style='text-align: center; color: #00b33c;'>Coronary Heart Disorder Diagnosis</p>", unsafe_allow_html=True)
    with col3:
        st.image("s-2.jpeg", width=200)
        st.write("<p style='text-align: center; color: #00b33c;'>Diabetes Diagnosis</p>", unsafe_allow_html=True)
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("s-3.jpeg", width=200)
        st.write("<p style='text-align: center; color: #00b33c;'>Chronic Kidney Disease Diagnosis</p>", unsafe_allow_html=True)
    with col5:
        st.image("s-4.jpeg", width=200)
        st.write("<p style='text-align: center; color: #00b33c;'>Heparus Liver Diagnosis</p>", unsafe_allow_html=True)
    with col6:
        st.image("s-5.jpeg", width=200)
        st.write("<p style='text-align: center; color: #00b33c;'>Explore DataBases and Relationships</p>", unsafe_allow_html=True)
    
    st.write('-------------------------------------------------------')
    st.markdown("<h2 style='color: #ff4d94;'>VDRL Founder</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("1@2x.png", width=250)
    with col2:
        st.markdown("""<div style='text-align: justify; color: #ff8080;'>
                     Hello, I am Vishesh Gupta. I work in Data Science and Data Analysis. 
                     I am pursuing a Master's in Data Analytics Engineering at Northeastern University 
                     in Boston, where I am currently studying Data Mining in Engineering, Computation and 
                     Visualization for Analytics under the guidance of 
                     <a href='https://coe.northeastern.edu/people/kamarthi-sagar/'>Prof. Sagar Kamarthi</a> 
                     and <a href='https://coe.northeastern.edu/people/radhakrishnan-srinivasan/'>
                     Prof. Sri RadhaKrishnan</a>. For an overview of my work, check out 
                     <a href='https://visheshgupta-ba.github.io/VisheshGupta/projects'>my projects</a>. 
                     If you are interested in data science and analytics research, then check 
                     <a href='https://visheshgupta-ba.github.io/VisheshGupta/readinglist.html'>my reading list</a> 
                     and <a href='https://visheshgupta-ba.github.io/VisheshGupta/blog'>blog</a>.
                  </div>""", unsafe_allow_html=True)
    
    st.write('-------------------------------------------------------')
    st.markdown(
        """
        <div style='text-align: center; color: #ff80bf'>
        Follow us on <a href='https://www.linkedin.com/in/ba-visheshgupta/' target='_blank' style='color:purple'>linkedin</a>, <a href='https://github.com/visheshgupta-BA/' target='_blank' style='color:purple'>github</a>, <a href='https://twitter.com/SudhirVishesh/' target='_blank' style='color:purple'>twitter</a>, <a href='https://www.facebook.com/profile.php?id=100009738763104' target='_blank' style='color:purple'>facebook</a> for updates and news about Vishesh Gupta's Diagnosis Labs!
        </div>
        """,
        unsafe_allow_html=True
    )
    
    
    st.write('-------------------------------------------------------')
    st.markdown("<div style='text-align: center;'>©2023 All right reserved. Vishesh Diagnostic & Research Centre Pvt. Ltd.</div>", unsafe_allow_html=True)
    
    
    
    
    
    
    
    
    
    



