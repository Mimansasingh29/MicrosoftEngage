#importing libraries
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


#defining a function named analysis
def analysis(df):
    header = st.container()
    dataset = st.container()
    features = st.container()
    model_training = st.container()
        
    #designing side navigation bar
    with st.sidebar:
        selected = option_menu(
        menu_title = "Analysis",
        options= ["Customer Segment", "Car Specification", "Price Analysis", "Other Specifications"],
        default_index = 0,
        styles = {
            "container": {"background-color": "bisque"},
        }
        )
    
    ### DATA CLEANING

    #Replacing null value in Make column with first name of Model
    df.insert(loc=1,                                                                         #making a column to contain first name of each model
              column='splitted_model',
              value= df["Model"].apply(lambda x: x.split()[0]))
    df["Make"].fillna(df["splitted_model"], inplace = True)

    #Dropping useless columns
    df =df.drop(['Unnamed: 0','Auto-Dimming_Rear-View_Mirror', 'Hill_Assist', 'Gear_Indicator', '3_Point_Seat-Belt_in_Middle_Rear_Seat', 'Ambient_Lightning', 'Cargo/Boot_Lights', 'Drive_Modes', 'Engine_Immobilizer', 'High_Speed_Alert_System', 'Lane_Watch_Camera/_Side_Mirror_Camera', 'Passenger_Side_Seat-Belt_Reminder', 'Seat_Back_Pockets', 'Voice_Recognition', 'Walk_Away_Auto_Car_Lock', 'ABS_(Anti-lock_Braking_System)', 'Headlight_Reminder', 'Adjustable_Headrests', 'Gross_Vehicle_Weight', 'Airbags', 'Door_Ajar_Warning', 'EBD_(Electronic_Brake-force_Distribution)', 'Fasten_Seat_Belt_Warning', 'Gear_Shift_Reminder', 'Compression_Ratio', 'Adjustable_Steering_Column', 'Other_Specs', 'Other_specs', 'Parking_Assistance', 'Key_Off_Reminder', 'USB_Compatibility', 'Android_Auto', 'Apple_CarPlay', 'Cigarette_Lighter', 'Infotainment_Screen', 'Multifunction_Steering_Wheel', 'Average_Speed', 'EBA_(Electronic_Brake_Assist)', 'Seat_Height_Adjustment', 'Navigation_System', 'Second_Row_AC_Vents', 'Tyre_Pressure_Monitoring_System', 'Rear_Center_Armrest', 'iPod_Compatibility', 'ESP_(Electronic_Stability_Program)', 'Cooled_Glove_Box', 'Recommended_Tyre_Pressure', 'Heated_Seats', 'Turbocharger', 'ISOFIX_(Child-Seat_Mount)', 'Rain_Sensing_Wipers', 'Paddle_Shifters', 'Leather_Wrapped_Steering', 'Automatic_Headlamps', 'Engine_Type', 'ASR_/_Traction_Control', 'Cruise_Control', 'USB_Ports', 'Heads-Up_Display', 'Welcome_Lights', 'Battery', 'Electric_Range', 'Handbrake', 'Instrument_Console', 'Low_Fuel_Warning', 'Minimum_Turning_Radius', 'Multifunction_Display', 'Sun_Visor', 'Third_Row_AC_Vents', 'Ventilation_System', 'Central_Locking', 'Child_Safety_Locks', 'Clock', 'Cup_Holders', 'Distance_to_Empty', 'Door_Pockets', 'Engine_Malfunction_Light', 'Extended_Warranty', 'FM_Radio', 'Fuel-lid_Opener', 'CD_/_MP3_/_DVD_Player', 'Bluetooth', 'Boot-lid_Opener', 'Aux-in_Compatibility', 'Average_Fuel_Consumption', 'Start_/_Stop_Button', '12v_Power_Outlet', 'Power_Steering', 'Power_Windows', 'Power_Seats', 'Keyless_Entry'], axis=1)
    
    #Dropping null values of useful columns 
    df = df.dropna(subset=['Width', 'Height', 'Wheelbase', 'Fuel_Tank_Capacity', 'Seating_Capacity', 'ARAI_Certified_Mileage', 'Torque', 'Drivetrain', 'Doors', 'Number_of_Airbags','Cylinders', 'Displacement'])
    
    #Converting datatype of columns
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

    
    #PLOTTING GRAPHS FOR DATA ANALYSIS

    #The code for Customer Segment part starts here
    if selected == "Customer Segment":
        col1, col2 = st.columns( [0.9, 0.1])
        with col1:
            #Plotting graph between car count and company   
            dic = {}                                                                    #making a dictionary to store data
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
            plt.title('Company Analysis', fontsize=40)
            plt.grid()
            st.pyplot(fig)
            st.write('The above graph represents the number of cars each companies make. It can be intepreted that Maruti Suzuki manufactures most number of cars followed by Hyundai and so on.', fontsize = 30)
            
            #plotting graph between car count vs price
            fig = plt.figure(figsize=(20,12))
            sns.histplot(data=df, x='Ex-Showroom_Price',bins=1000,alpha=.5, color='darkblue')                 #plotting histogram
            plt.title('Price Analysis',fontsize=40)
            plt.xticks(fontsize =20)
            plt.yticks(fontsize =20)
            plt.ylabel('Count', fontsize =20)
            plt.xlabel('Price', fontsize =20)
            plt.xlim(0, 5000000)
            plt.grid()
            st.pyplot(fig)
            st.write('The above graph shows car price data which clearly represents that number of cars is maximum for a price after which car produced is decreased.', fontsize=30)
    
    
    #The code for Car Specification part starts here
    if selected == "Car Specification":
        col1, col2 = st.columns( [0.9, 0.1])
        with col1:
            #plotting graph between car count vs displacement
            st.header('Engine Analysis')
            dic1 = {}                                                                           #making dictionary to store data
            for displacement in df['Displacement'].unique():
                dic1[displacement] = sum(df['Displacement']==displacement)
            displacement = sorted(dic1.items(), key=lambda x: x[1], reverse=True)[:15]

            fig = plt.figure(figsize=(14,8))
            plt.bar(range(len(displacement)),[val[1] for val in displacement], align='center', color= 'green', edgecolor='black')
            plt.xticks(range(len(displacement)),[val[0] for val in displacement])
            plt.yticks(fontsize= 18)
            plt.xticks(fontsize= 18,rotation=70)
            plt.ylabel('Number of cars', fontsize=20)
            plt.xlabel('Displacement(in cc)', fontsize=20)
            st.pyplot(fig)
            st.write('The above bar graph shows that maximum number of cars in market is of 1197cc followed by cars of 1498cc.', fontsize=30) 

            #plotting graph between fuel type and car count
            st.header('Fuel Analysis')
            fig = plt.figure(figsize=(14,8))
            fuel_type = df['Fuel_Type'].unique()
            car_count = df['Fuel_Type'].value_counts()
            plt.plot(fuel_type, car_count, marker='o', color='red')
            plt.ylabel("Car Count", fontsize=20)
            plt.yticks(fontsize= 18)
            plt.xticks(fontsize= 18)
            for xy in zip(fuel_type, car_count):                                                    
                plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='data', fontsize=18) 
            plt.grid()
            st.pyplot(fig)
        
            #plotting graph between fuel tank capacity and type
            fig = plt.figure(figsize=(14,8))
            tank_capacity= df['Fuel_Tank_Capacity']
            fuel_type = df['Fuel_Type']
            plt.ylabel('tank_capacity', fontsize=20)
            plt.xlabel('fuel_type', fontsize=20)
            plt.xticks(fontsize=14, rotation=300)
            plt.bar( fuel_type, tank_capacity, color = 'salmon')
            st.pyplot(fig)
            st.write('This shows that cars with petrol fuel type is the most number of cars produced followed by CNG and number of cars with CNG+Petrol is only 2. Also, Petrol cars and diesel cars has same and highest tank capacity.', fontsize=30)

             #plotting graph between mileage and car count
            st.header('Car Potential Analysis')
            fig=plt.figure(figsize=(14,8))
            car_count = df['ARAI_Certified_Mileage'].value_counts()
            plt.xlim(0 , 35)
            plt.ylabel('Car count', fontsize=20)
            plt.xlabel('Mileage', fontsize=20)
            plt.yticks(fontsize= 18)
            plt.xticks(fontsize= 18)
            sns.histplot(data=df, x='ARAI_Certified_Mileage',bins=1000,alpha=.6, color='purple')
            st.pyplot(fig)
            st.write('The graph shows number of cars produced with increasing mileage. It is visible that mileage with average value between 15-20 has highest number of cars', fontsize=30)

            #plotting pie graph for drivetrain analysis
            st.header('Drivetrain Analysis')
            fig = plt.figure(figsize=(14,8))
            drivetrain = df["Drivetrain"].unique()
            number_of_cars = df['Drivetrain'].value_counts()
            fig = px.pie(drivetrain, values =number_of_cars, names= drivetrain)
            fig.update_layout(
            title="<b>Drivetrain relation with car counts</b>")
            st.plotly_chart(fig)
            st.write('Four typeds of drivetrain are represented on the above graph which clearly shows that FWD drivetrain is most produced. On hovering on each part, the analysis of each part is visible', fontsize=30)

            #plotting graph for body type count
            st.header('Body Type Analysis')
            fig = plt.figure(figsize=(16,8))
            sns.countplot(data=df, y='Body_Type',alpha=.6,color='purple')
            plt.title('Cars vs car body type',fontsize=40)
            plt.ylabel('Body Type', fontsize=20)
            plt.xlabel('Car count', fontsize=18)
            plt.xticks(fontsize=18)
            plt.yticks(fontsize=18)
            plt.grid()
            st.pyplot(fig)
            st.write('SUV body type is most preffered. This gives the idea to user which car body material should one choose.', fontsize=30)
    
    #The code for Price Analysis page starts
    if selected == 'Price Analysis': 
        col1, col2 = st.columns( [0.9, 0.1])
        with col1:
            #plotting graph between displacement and price
            st.header('Engine Price Analysis')
            fig = plt.figure(figsize=(14,8))
            displacement = df['Displacement']
            price = df['Ex-Showroom_Price']
            plt.scatter(displacement, price, color='peru')                                            #plotting scatter plot
            plt.ylabel('Price', fontsize=20)
            plt.xlabel('Displacement(in cc)', fontsize=20)
            plt.yticks(fontsize= 18)
            plt.xticks(fontsize= 18)
            plt.grid()
            st.pyplot(fig)
            st.write('It is evident that as displacement of car increases, the price also increases. Also, between 1000cc to 3000cc, maximum number of car is produced.', fontsize=30)
    
            #plotting graph between mileage and price
            st.header('Car Potential Price Analysis')
            fig = plt.figure(figsize=(14,8))
            price = df['Ex-Showroom_Price']
            Mileage = df['ARAI_Certified_Mileage']
            plt.ylabel('Price', fontsize=20)
            plt.xlabel('Mileage', fontsize=20)
            plt.xlim(0 , 35)
            plt.yticks(fontsize= 18)
            plt.xticks(fontsize= 18)
            plt.scatter( Mileage,price, color= 'green')
            st.pyplot(fig)
            st.write('Cars with less mileage have more price. Also, some cars with mileage between 20-25 has more price due to other deciding parameters other than mileage.', fontsize=30)
    
            #plotting graph between price and body type
            st.header('Body Type Price Analysis')
            fig = plt.figure(figsize=(14,8))
            price = df['Ex-Showroom_Price']
            body_type = df['Body_Type']
            plt.ylabel('Price', fontsize =20)
            plt.xlabel('Body Type', fontsize=20)
            plt.xticks(fontsize=18, rotation=90)
            plt.yticks(fontsize=18)
            plt.bar( body_type,price)
            st.pyplot(fig)
            st.write('Sedan is the most expensive body type whereas SUV which was most produced has average price.', fontsize=30)
    
    
    #The code for Other Specification part starts here
    if selected == 'Other Specifications':
        col1, col2 = st.columns( [0.9, 0.1])
        with col1:
            #3D graph between components of company cars
            st.header('Components Analysis')
            df['Car_name'] = df['Make']+ ',' +df['Model']
            st.write('This graph can be zoomed in, out and can be rotated at any angle for better analysis. Hovering on any point will give the details about the parameters of car and the car name', fontsize=30)
            plt.figure()
            fig= px.scatter_3d(df, x='Number_of_Airbags', z='Seating_Capacity', y='Cylinders',color='Car_name',width=800,height=750)
            fig.update_layout(showlegend=True)
            plt.savefig('graph1.png')
            st.plotly_chart(fig)

            #3D graph between dimension of cars 
            st.header('Dimension Analysis')
            st.write('This graph can be zoomed in, out and can be rotated at any angle for better analysis. Hovering on any point will give the details about the parameters of car and the car name', fontsize=30)
            plt.figure()
            fig= px.scatter_3d(df, x='Length', z='Width', y='Height',color='Car_name',width=800,height=750)
            fig.update_layout(scene = dict(
            xaxis = dict(range=[3000,6000],),
                         yaxis = dict(range=[1000,2000],),
                         zaxis = dict(range=[1200,2000],),),showlegend=True)
            plt.savefig("graph.png")
            st.plotly_chart(fig)
    
            #heatmap between parameters for data analysis
            st.header('Coorelation Analysis')
            fig = plt.figure(figsize=(14,8))
            sns.heatmap(df.corr(), annot=True, fmt='.2%', cmap= "PiYG")
            plt.title('Correlation between differet variable',fontsize=20)
            plt.xticks(fontsize=18, rotation=270)
            plt.yticks(fontsize=18)
            st.pyplot(fig)


    
