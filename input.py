# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:43:27 2023

@author: barry
"""

import streamlit as st
import pandas as pd

# Set page title
st.set_page_config(page_title="Heart Data Page")

# Define function to save data to .csv file
def save_data(data):
    df = pd.DataFrame(data, columns=["Name", "age", "gender","height","weight","aphi","aplo","cholesterol","glucose","smoke","alcohol","active","cardio"])
    df.to_csv("data.csv", index=False)

# Create page header
st.header("Heart Data")

# Create input fields for user to enter data
name = st.text_input("Name")
age = st.number_input("age")
gender = st.number_input("Gender: 1 = Male 2 = Female")
height = st.number_input("Height in inches")
weight = st.number_input("Weight in pounds")
aphi = st.number_input("Systolic Blood Pressure")
aplo = st.number_input("Diastolic Blood Pressure")
cholesterol = st.number_input("Cholesterol Level")
glucose = st.number_input("Glucose level")
smoke = st.number_input("Smoke: 1 is Yes, 0 is No")
alcohol = st.number_input("3 or more drinks per week = 1, Less than = 0")
active = st.number_input("Walk more than 1 mile per week = 1 Less = 0")
cardio = st.number_input("3 or more cardio sessions per week = 1 Less = 0")
# Create button to submit data and save to .csv file
if st.button("Submit"):
    # Save data
    data = {"Name": [name], "age": [age], "gender": [gender],"height":[height],"weight":[weight], "aphi": [aphi], "aplo": [aplo], "cholesterol":[cholesterol], "glucose": [glucose], "smoke": [smoke], "alcohol": [alcohol], "active": [active], "cardio": [cardio]}
    #data = {"Name": [name], "age": [age], "gender": [gender], "height": [height], "weight": [weight], "aphi": [aphi], "aplo": [aplo], "cholesterol": [cholesterol], "glucose": [glucose], "smoke": [smoke], "alcohol": [alcohol], "active": [active], "cardio"[cardio]}

    save_data(data)
    # Display confirmation message
    st.success("Data saved to data.csv file!")
