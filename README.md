# MicrosoftEngage
> A webapp designed for data analysis of automative industry using python

## Dataset used:
[cars_engage_2022.csv](https://github.com/Mimansasingh29/MicrosoftEngage/files/8785798/cars_engage_2022.csv)

## Prerequisites
##### You must have following installed:
* Anaconda Distribution
* Jupyter Notebook 
* Visual Studio Code / PyCharm
##### Following libraries of python should also be installed:
* Streamlit
* Pandas
* Numpy
* Matplotlib
* Seaborn
* Plotly Express

## Features
* Displays dataset of the uploaded file
* Analyse the data and displays different graphs.

## Demo
* **HOME PAGE**
![Screenshot (73)](https://user-images.githubusercontent.com/76276453/170674337-bb8b2ed4-d438-415e-845f-3ba2df0f6aa5.png)


* **ABOUT PAGE**
![Screenshot (74)](https://user-images.githubusercontent.com/76276453/170674619-3416edd4-c260-42f0-82d4-c53dc0dbdc34.png)


* **CONTACT PAGE**
![Screenshot (75)](https://user-images.githubusercontent.com/76276453/170674656-196b4f0f-f26a-4b1e-b44b-4978b651691d.png)


* **UPLOADING SECTION**
![Screenshot (76)](https://user-images.githubusercontent.com/76276453/170674752-4d214592-f1a9-4a6b-a3d0-4ad253e68f4a.png)


* **DISPLAYING FILE DETAILS** 
![Screenshot (77)](https://user-images.githubusercontent.com/76276453/170674836-55becf79-7684-4b5e-af26-6dfd8ec64b10.png)


* **CUSTOMER SEGMENT**
![Screenshot (78)](https://user-images.githubusercontent.com/76276453/170674960-0f1ed31e-9a03-4850-b940-6c19d27f2c2b.png)


* **CAR SPECIFICATION SEGMENT**
![Screenshot (82)](https://user-images.githubusercontent.com/76276453/170675072-ed66a5e9-24f7-42cc-8d04-317ca287e07a.png)


* **PRICE ANALYSIS SEGMENT**
![Screenshot (86)](https://user-images.githubusercontent.com/76276453/170675148-76b64d04-7177-40a6-b421-1d1139bea5b0.png)


* **3D GRAPHS**
![Screenshot (87)](https://user-images.githubusercontent.com/76276453/170675232-2c1e0e49-9e0c-474c-80fd-c997c20a7004.png)
![Screenshot (88)](https://user-images.githubusercontent.com/76276453/170675249-b396f42a-bbca-402b-b4b6-64cc52b4f535.png)


## Data Analysis
Several steps used for analysis are as follows:
1. Importing Libraries
2. Dealing with Missing Values
3. Data Cleaning
4. Explorayory Data Analysis

## Importing Libraries
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns  
import plotly.express as px  
  
## Analysis
1. Bar Graph representing number of cars companies manufacture
   ![03c9e724f34b9e1ef48f933070948c9eb674f8b69e13eeef2ad71e65](https://user-images.githubusercontent.com/76276453/170681367-712f862b-9a0d-4700-98cf-47c23e015aea.png)

2. Histogram showing the variation of number of cars with price
   ![068ae77f651ff85e50bdf260b72fd43452cf000f4a8f99ef354ee8ce](https://user-images.githubusercontent.com/76276453/170681425-89f6e03a-e4aa-4a55-9c87-101822d2bc23.png)
   
3. Bar Graph showing displacement relation with the car count present
   ![e866a376ff0abf63baeac8bacbe55fb0e32d6e0c18d2331f27e9ff0b](https://user-images.githubusercontent.com/76276453/170681513-6b928824-9b05-4a67-bd04-c05ecb42bc7f.png)

4. Line Chart for car count on the basis of fuel type
   ![faec3245f2ec6972234700de37c56657bfe7422b803dc51ebd6e417a](https://user-images.githubusercontent.com/76276453/170681559-c8150e9a-3f46-41c1-b274-8d53038d63ed.png)

5. Bar Graph for Tank Capacity of cars with different fuel type
   ![074b4c91fc30a00609260454e1b8c9f81e10c74b45e010357a762c3b](https://user-images.githubusercontent.com/76276453/170681593-650383ce-4174-4cd1-9328-8175972f7d71.png)

6. Histogram for Mileage relation with the number of cars 
   ![3c864c9e1ec0aed1b326dfe5734659c6448010c109b63776b1af7bb4](https://user-images.githubusercontent.com/76276453/170681701-86beaa18-5d52-47ae-a298-34018a5af6ed.png)

7. Pie Graph for Drivetrain where value represents number of cars
   ![newplot](https://user-images.githubusercontent.com/76276453/170682711-79ac638f-6bf2-4a96-88c5-8c34255817b0.png)
   
8. Horizontal bar graph for body type
   ![ccf529d4d40440be0700e99fe8fbbff472a21675c0ee2dab45819adc](https://user-images.githubusercontent.com/76276453/170682882-30bc9221-93f3-4c77-a3af-481fa94dfe02.png)

9. Scatter plot for price and displacement analysis'
   ![fb1ee59556ecc54d654b7b1a1ecb8ed613dad8ba8da9da0d241474f4](https://user-images.githubusercontent.com/76276453/170682987-4e75b1b3-00f8-4930-8fbc-0ac619e38128.png)

10. Scatter plot for Mileage and price realtion
    ![c2812e22fe786b11e0c5133ab312f81714cf38c7f1657b4acd8ada02](https://user-images.githubusercontent.com/76276453/170683140-0834b166-f1c2-4f44-b6dc-336bada4925f.png)

11. Bar graph for variation of price with body type
    ![db2d08528d434f8d2c77a0e716dbce04cbd2b67096c4a1b80a067327](https://user-images.githubusercontent.com/76276453/170683242-1c786f1c-e85f-44f5-ae4f-bc25c914ad7d.png)

12. 3D graph to show data of number of airbags, seating capacity and number of cylinders for different models
    ![newplot (3)](https://user-images.githubusercontent.com/76276453/170683734-e32d4f02-d2c1-4703-9fe1-25fa14574d1d.png)

13. 3D graph for data analysis of dimension of cars 
    ![newplot (4)](https://user-images.githubusercontent.com/76276453/170683868-c31811ef-bcdb-4a79-ad0d-edab26d20873.png)

14. Coorelation Map for relation between different parameters
    ![fb990f62143e32e522f8fa06e6e14743491411836fab4c544e3b0582](https://user-images.githubusercontent.com/76276453/170683998-2c99cdf9-9503-4d81-a6af-5855dc9eed4e.png)

## Conclusion
This app is a generic app which can analyse any type of data provided with some restriction to the columns present in dataset. It uses different python libraries to analyse the data, clean and store it to make different types of graph which will help the user to analyse dataset. A total of 14 graphs is displayed in the app, each representing different parameters and relations, 'number of cars' and 'price' becoming the most important factor. 

## Installation
pip install streamlit  
pip install streamlit-option-menu  

## To run the app in local system
1. Open the anaconda terminal:
2. Clone the GitHub repository into your local device and move into the directory.
   Then write:
   cd 'directory path' ----->   streamlit run 'File name.py' 
   
![Anaconda Prompt (anaconda3) - streamlit  run Data_Analysis1 py 5_29_2022 3_06_43 AM](https://user-images.githubusercontent.com/76276453/170843625-81caa277-6bfe-4efb-87e0-75f8b72de71a.png)









