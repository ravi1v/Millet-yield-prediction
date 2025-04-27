import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('C:\\Users\\vrsha\\Crop yield prediction\\Millet yield pred.joblib')

# Streamlit App UI
st.title(' 🌾Millet Yield Prediction🌾')
st.markdown("This app predicts the yield of millet based on various input features.")

# Input fields for the features based on your dataset
moisture = st.number_input('Moisture', min_value=0.0, max_value=100.0, value=12.8)
rainfall = st.number_input('Rainfall (in mm)', min_value=0.0, max_value=500.0, value=0.012)
humidity = st.number_input('Average Humidity (%)', min_value=0, max_value=100, value=57)
mean_temp = st.number_input('Mean Temperature (°C)', min_value=-50, max_value=100, value=62)
max_temp = st.number_input('Max Temperature (°C)', min_value=-50, max_value=100, value=71)
min_temp = st.number_input('Min Temperature (°C)', min_value=-50, max_value=100, value=52)
alkaline = st.number_input('Alkaline Soil (0 = No, 1 = Yes)', min_value=0, max_value=1, value=0)
sandy = st.number_input('Sandy Soil (0 = No, 1 = Yes)', min_value=0, max_value=1, value=1)
chalky = st.number_input('Chalky Soil (0 = No, 1 = Yes)', min_value=0, max_value=1, value=0)
clay = st.number_input('Clay Soil (0 = No, 1 = Yes)', min_value=0, max_value=1, value=0)

# Prepare input data for prediction
input_data = np.array([[moisture, rainfall, humidity, mean_temp, max_temp, min_temp, alkaline, sandy, chalky, clay]])

# Debugging: Check the shape of the input data
st.write("Input data shape:", input_data.shape)

# Predict on button click
if st.button('🔍🔍 Predict Millet Yield 🔍🔍'):
    # Make sure input_data has the correct shape (1, n_features)
    if input_data.shape == (1, 10):  # Ensure there are 10 features
        yield_prediction = model.predict(input_data)
        st.write(f" 🌾 Predicted Millet Yield 🌾: {yield_prediction[0]:.2f} tonnes per hectare")
    else:
        st.error("Error: The number of input features does not match the model's expectations.")
