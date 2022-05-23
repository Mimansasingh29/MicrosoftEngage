from secrets import choice
from turtle import color, position
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from streamlit_option_menu import option_menu
from  PIL import Image
import streamlit.components.v1 as html
import io 
import os.path


header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

# horizontal nav bar
selected = option_menu(
    menu_title = "Car Analytics",
    options= ["Home", "About", "Contact"],
    menu_icon = "cast",
    orientation = "horizontal",
    default_index = 0,
    styles = {
        "container": {"background-color": "bisque"},
    }
)

if selected == 'Home':
    data_file = st.file_uploader("Choose a file", type=["csv"])
    if data_file is not None:
        file_details = {"filename":data_file.name, "filetype":data_file.type, "filesize":data_file.size}

        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)

        st.button("Get Analysis")
         #   link = '(C:\Users\HP\Desktop\tutorial project\streamlite project\ms_page_second.py)'
          #  st.markdown(link, unsafe_allow_html=True)'


#logo = Image.open(r'C:\Users\HP\Pictures\carlogo.jpg')
if selected == 'About':
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">About the Creator</p>', unsafe_allow_html=True)    
    st.write("The automotive industry comprises a wide range of companies and organizations involved in the design, development, manufacturing, marketing, and selling of motor vehicles.[1] It is one of the world's largest industries by revenue (from 16 % such as in France up to 40 % to countries like Slovakia). It is also the industry with the highest spending on research & development. Seeing the rise in production of automobiles, it is important to analyse the data of the automobiles and present it to population to make life and choices of people easier.")   

elif selected == "Contact":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Contact detaiks:</p>', unsafe_allow_html=True)
    st.write("Phone number: 873429****, 833098****")
    st.write("Email address: automobile.industry1@gmail.com")
# navigation bar ending  

