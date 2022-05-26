#importing libraries
from secrets import choice
from turtle import color, position
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from Data_Analysis2 import analysis 


header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

# designing horizontal navignation bar
selected = option_menu(
    menu_title = "Car Analytics",
    options= ["Home", "About", "Contact"],
    menu_icon = "cast",
    default_index = 0,
    orientation = "horizontal",
    styles = {
        "container": {"background-color": "bisque"},
    }
)

if selected == 'Home':
    data_file = st.file_uploader("Choose a file", type=["csv"])                            # making file upload option
    if data_file is not None:
        file_details = {"filename":data_file.name, "filetype":data_file.type, "filesize":data_file.size}

        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)

        analysis(df)


if selected == 'About':
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">About the App</p>', unsafe_allow_html=True)    
    st.write("The automotive industry comprises a wide range of companies and organizations involved in the design, development, manufacturing, marketing, and selling of motor vehicles.It is one of the world's largest industries by revenue. It is also the industry with the highest spending on research & development. Seeing the rise in production of automobiles, it is important to analyse the data of the automobiles. This app gives you detailed study about the different parameters of cars, graph for their relation and conclusion. This will help the user to get a clear and detailed overview of the automobile industry.")   


elif selected == "Contact":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Contact details:</p>', unsafe_allow_html=True)
    st.write("Phone number: 873429****, 833098****")
    st.write("Email address: automobile.industry1@gmail.com")
# navigation bar ending 