from ctypes import alignment
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
import altair as alt
import plotly.graph_objects as go


header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()


df = pd.read_csv(r"C:\Users\HP\Downloads\cars_engage_2022.csv")

#side navigation bar
with st.sidebar:
    selected = option_menu(
    menu_title = "Analysis",
    options= ["Customer Segment", "Car Specification", "Price Analysis", "Other Specifications"],
    default_index = 0,
    styles = {
        "container": {"background-color": "bisque"},
    }
    )

#dropping null values of useful columns 
df = df.dropna(subset=['Width', 'Height', 'Wheelbase', 'Fuel_Tank_Capacity', 'Seating_Capacity', 'Torque', 'Drivetrain', 'Doors', 'Seating_Capacity', 'Number_of_Airbags','Cylinders', 'Displacement'])
#cleaning data
df['Ex-Showroom_Price'] = df["Ex-Showroom_Price"].apply(lambda x:int( x[4:].replace(',','')))
df["Height"] = df["Height"].astype(str).apply(lambda x: x.replace(' mm','')).astype(float)
df["Length"] = df["Length"].astype(str).apply(lambda x: x.replace(' mm','')).astype(float)
df["Width"] = df["Width"].astype(str).apply(lambda x: x.replace(' mm','')).astype(float)
df["Wheelbase"] = df["Wheelbase"].astype(str).apply(lambda x: x.replace(' mm','')).astype(float)
df['Fuel_Tank_Capacity'] = df['Fuel_Tank_Capacity'].astype(str).apply(lambda x: x.replace(' litres','')).astype(float)
df["Displacement"] = df["Displacement"].astype(str).apply(lambda x: x.replace(' cc','')).astype(float)

df['Number_of_Airbags'] = df['Number_of_Airbags'].fillna(0)
#dropping null values and converting it to integer
df['Doors'] = df['Doors'].astype(int)
df['Seating_Capacity'] = df['Seating_Capacity'].astype(int)
df['Number_of_Airbags'] = df['Number_of_Airbags'].astype(int)
df['Cylinders'] = df['Cylinders'].astype(int)
df['Displacement'] = df['Displacement'].astype(int)

df.loc[df.ARAI_Certified_Mileage == '9.8-10.0 km/litre','ARAI_Certified_Mileage'] = '10'
df.loc[df.ARAI_Certified_Mileage == '10kmpl km/litre','ARAI_Certified_Mileage'] = '10'
df.loc[df.ARAI_Certified_Mileage == '22.4-21.9 km/litre', 'ARAI_Certified_Mileage'] = '22'
df['ARAI_Certified_Mileage'] = df['ARAI_Certified_Mileage'].dropna().astype(str).apply(lambda x: x.replace(' km/litre','')) .astype(float) 


HP = df.Power.str.extract(r'(\d{1,4}).*').astype(int) * 0.98632
HP = HP.apply(lambda x: round(x,2))
TQ = df.Torque.dropna().str.extract(r'(\d{1,4}).*').astype(int)
TQ = TQ.apply(lambda x: round(x,2))
df.Torque = TQ
df.Power = HP
#cleaning data

if selected == "Customer Segment":
    col1, col2 = st.columns( [0.9, 0.1])
    with col1:
        #plotting graph between car count and company by dictionary
        dic = {}
        for make in df['Make'].unique():
            dic[make] = sum(df['Make']==make)
            car_statistics = sorted(dic.items(), key=lambda x: x[1], reverse=True)[:20]

        fig = plt.figure(figsize=(20,12))
        plt.bar(range(len(car_statistics)), [val[1] for val in car_statistics], align='center')
        plt.xticks(range(len(car_statistics)), [val[0] for val in car_statistics])
        plt.xticks(fontsize =20,rotation=70)
        plt.yticks(fontsize =20)
        plt.ylabel('Number_of_cars', fontsize =20)
        plt.xlabel('Company_Name', fontsize =20)
        plt.title('Car count vs company', fontsize=40)
        plt.grid()
        st.pyplot(fig)

        st.write('The above graph represents the number of cars each companies make. It can be intepreted that Maruti Suzuki manufactures most number of cars followed by Hyundai and so on.', fontsize = 30)

        #plotting graph between car count vs price
        fig = plt.figure(figsize=(20,12))
        sns.histplot(data=df, x='Ex-Showroom_Price',bins=1000,alpha=.5, color='darkblue')
        plt.title('Histogram of cars price data',fontsize=40)
        plt.xticks(fontsize =20)
        plt.yticks(fontsize =20)
        plt.ylabel('Count', fontsize =20)
        plt.xlabel('Price', fontsize =20)
        plt.xlim(0, 5000000)
        plt.grid()
        st.pyplot(fig)

        st.write('The above graph shows car price data i.e., number of cars in the market with respect to price.', fontsize=30)


if selected == "Car Specification":
    st.header('Engine_Type')
    col1, col2 = st.columns( [0.9, 0.1])
    with col1:
        dic1 = {}
        for displacement in df['Displacement'].unique():
            dic1[displacement] = sum(df['Displacement']==displacement)

        displacement = sorted(dic1.items(), key=lambda x: x[1], reverse=True)[:15]
        #plotting bar graph for number of cars vs engine type (displacement)
        fig = plt.figure(figsize=(16,12))
        plt.bar(range(len(displacement)),[val[1] for val in displacement], align='center', color= 'green', edgecolor='black')
        plt.xticks(range(len(displacement)),[val[0] for val in displacement])
        plt.yticks(fontsize= 18)
        plt.xticks(fontsize= 18,rotation=70)
        plt.ylabel('Number_of_cars', fontsize=25)
        plt.xlabel('Displacement(in cc)', fontsize=25)
        st.pyplot(fig)
    

        st.header('Fuel Type')
        fig = plt.figure(figsize=(14,8))
        fuel_type = df['Fuel_Type'].unique()
        car_count = df['Fuel_Type'].value_counts()
        plt.plot(fuel_type, car_count, marker='o', color='red')
        plt.ylabel("Car_Count", fontsize=25)
        plt.yticks(fontsize= 18)
        plt.xticks(fontsize= 18)
        for xy in zip(fuel_type, car_count):                               
            plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') 
        plt.grid()
        st.pyplot(fig)


        fig = plt.figure(figsize=(14,8))
        tank_capacity= df['Fuel_Tank_Capacity']
        fuel_type = df['Fuel_Type']
        plt.ylabel('tank_capacity', fontsize=20)
        plt.xlabel('fuel_type', fontsize=20)
        plt.xticks(fontsize=18, rotation=300)
        plt.bar( fuel_type, tank_capacity, color = 'salmon')
        st.pyplot(fig)


        st.header('Mileage')
        fig= plt.figure(figsize=(14,8))
        car_count = df['ARAI_Certified_Mileage'].value_counts()
        plt.xlim(0 , 35)
        plt.ylim(0 , 20)
        plt.ylabel('Mileage', fontsize=20)
        plt.xlabel('car_count', fontsize=20)
        plt.yticks(fontsize= 18)
        plt.xticks(fontsize= 18)
        plt.plot(car_count,  linestyle='none', marker='o')
        st.pyplot(fig)


        st.header('Drivetrain')
        fig = plt.figure(figsize=(14,8))
        drivetrain = df["Drivetrain"].unique()
        number_of_cars = df['Drivetrain'].value_counts()
        # Creating autocpt arguments
        def func(pct, allvalues):
            absolute = int(pct / 100.*np.sum(allvalues))
            return "{:.1f}%\n({:d})".format(pct, absolute)
        ex = (0.1, 0.0, 0.2, 0.3)
        plt.pie(number_of_cars, explode=ex, autopct = lambda pct: func(pct, number_of_cars), shadow = True, labels=drivetrain)
        st.pyplot(fig)


        st.header('Body Type')
        fig = plt.figure(figsize=(14,8))
        sns.countplot(data=df, y='Body_Type',alpha=.6,color='purple')
        plt.title('Cars vs car body type',fontsize=20)
        plt.xticks(fontsize=18)
        plt.yticks(fontsize=18)
        st.pyplot(fig)


    st.write('The following graphs gives the detailed analysis about cars. The factors which are mainly responsible for decision of users are represented in these graphs. Starting with engine type, fuel type, Mileage, users can easily analyse to know about different cars.')


if selected == 'Price Analysis':
    col1, col2 = st.columns( [0.9, 0.1])
    with col1:
        st.header('Engine Type')
        fig = plt.figure(figsize=(14,8))
        displacement = df['Displacement']
        price = df['Ex-Showroom_Price']
        plt.scatter(displacement, price, color='peru')
        plt.ylabel('Ex-Showroom_Price', fontsize=20)
        plt.xlabel('Displacement', fontsize=20)
        plt.yticks(fontsize= 18)
        plt.xticks(fontsize= 18)
        plt.grid()
        st.pyplot(fig)

        st.header('Mileage')
        fig = plt.figure(figsize=(14,8))
        price = df['Ex-Showroom_Price']
        Mileage = df['ARAI_Certified_Mileage']
        plt.ylabel('price', fontsize=20)
        plt.xlabel('Mileage', fontsize=20)
        plt.xlim(0 , 35)
        plt.yticks(fontsize= 18)
        plt.xticks(fontsize= 18)
        plt.scatter( Mileage,price, color= 'green')
        st.pyplot(fig)

        st.header('Body Type')
        fig = plt.figure(figsize=(14,8))
        price = df['Ex-Showroom_Price']
        body_type = df['Body_Type']
        plt.ylabel('price', fontsize =20)
        plt.xlabel('body_type', fontsize=20)
        plt.xticks(fontsize=18, rotation=300)
        plt.yticks(fontsize=18)
        plt.bar( body_type,price)
        st.pyplot(fig)

if selected == 'Other Specifications':
    col1, col2 = st.columns( [0.9, 0.1])
    with col1:
        #relation between components of company cars
        st.header('3D plots for some parameters')
        st.write('Between Airbags, Cylinders and Seating capacity')
        plt.figure()
        fig= px.scatter_3d(df, x='Number_of_Airbags', z='Seating_Capacity', y='Cylinders',color='Make',width=800,height=750)
        fig.update_layout(showlegend=True)
        plt.savefig('graph1.png')
        st.plotly_chart(fig)

        st.write('Between dimension of car body')
        plt.figure()
        fig= px.scatter_3d(df, x='Length', z='Width', y='Height',color='Make',width=800,height=750)
        fig.update_layout(scene = dict(
        xaxis = dict(range=[3000,6000],),
                     yaxis = dict(range=[1000,2000],),
                     zaxis = dict(range=[1200,2000],),),showlegend=True)
        plt.savefig("graph.png")
        st.plotly_chart(fig)

        st.header('Coorelation between different parameters')
        fig = plt.figure(figsize=(22,14))
        sns.heatmap(df.corr(), annot=True, fmt='.2%', cmap= "PiYG")
        plt.title('Correlation between differet variable',fontsize=20)
        plt.xticks(fontsize=18, rotation=300)
        plt.yticks(fontsize=18)
        st.pyplot(fig)
