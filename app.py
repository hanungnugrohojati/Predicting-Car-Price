import pandas as pd
import pickle as pk
import streamlit as st

# Load the trained model
with open('car_price_model.pkl', 'rb') as model_file:
    model = pk.load(model_file)

# Upload Data
cars_data = pd.read_csv('Car_price.csv')

# Streamlit Page Setup
st.title('Predicting Car Price Web')

st.sidebar.header('Feature Selecting')
st.image('https://hips.hearstapps.com/hmg-prod/images/future-cars-679d3400f197f.jpg?crop=1.00xw:0.899xh;0,0.0575xh.jpg')
st.info('Predicting Car Price Based on Specifications to Help Optimize Pricing in Automobile Companies')

st.sidebar.info('Easy Application for Predicting Car Price')

# Mapping features (as you have already set)
# (Include all the mappings for 'Manufacturer', 'Model', 'Category', etc.)

# Collect input from the user
Manufacturer = st.selectbox('Manufacturer', m1)
Model = st.selectbox('Model', mm1)
Category = st.selectbox('Category', c1)
Leather = st.selectbox('Leather interior', l1)
Fuel = st.selectbox('Fuel type', f1)
Gear = st.selectbox('Gear box type', g1)
Drive = st.selectbox('Drive wheels', d1)
Wheel = st.selectbox('Wheel', w1)
Color = st.selectbox('Color', cc1)
Engine = st.selectbox('Engine volume', [3.5, 3. , 1.3, 2.5, 2. , 1.8, 2.4, 1.6, 2.2, 1.5, 3.3, 1.4, 2.3, 3.2, 1.2, 1.7, 2.9, 1.9, 2.7, 2.8, 2.1, 1. , 0.8, 3.4, 2.6, 1.1])
Airbags = st.selectbox('Airbags', [12, 8, 2, 0, 4, 6, 10, 3, 1, 16, 5, 7, 9, 11, 14, 15, 13])
Age = st.number_input('Age')
Mileage = st.number_input('Mileage')
Levy = st.number_input('Levy')

# Create DataFrame
df = pd.DataFrame({'Manufacturer': Manufacturer, 'Model': Model, 'Category': Category, 
                   'Leather interior': Leather, 'Fuel type': Fuel, 'Mileage': Mileage,
                   'Gear box type': Gear, 'Drive wheels': Drive, 'Wheel': Wheel, 'Color': Color,
                   'Levy': Levy, 'Engine volume': Engine, 'Airbags': Airbags, 'Age': Age}, index=[0])

# Button to trigger prediction
if st.sidebar.button('Predict Price'):
    # Make prediction
    Pre = model.predict(df)
    st.subheader(f'Predicted Price: ${Pre[0]:,.2f}')
    st.table(df)

