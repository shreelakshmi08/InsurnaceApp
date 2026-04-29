import streamlit as st
import pickle
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load model
model = pickle.load(open('gb_model.pkl', 'rb'))

# Title
st.title('💰 Insurance Price Prediction App')

st.write("Enter details below to predict insurance cost")

# User Inputs
age = st.number_input('Age', min_value=1, max_value=100, value=25)
gender = st.selectbox('Gender', ('male', 'female'))
bmi = st.number_input('BMI', min_value=10.0, max_value=80.0, value=25.0)
children = st.number_input('Children', min_value=0, max_value=10, value=0)
smoker = st.selectbox('Smoker', ('yes', 'no'))
region = st.selectbox('Region', ('southeast', 'southwest', 'northwest', 'northeast'))

# Predict Button
if st.button('Predict'):

    # Create dataframe (same format as training)
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [gender],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })

    # One-hot encoding
    input_data = pd.get_dummies(input_data)

    # Match model features
    input_data = input_data.reindex(columns=model.feature_names_in_, fill_value=0)

    # Prediction
    prediction = model.predict(input_data)
    output = round(prediction[0], 2)

    st.success(f'💸 Estimated Insurance Cost: ${output}')

    # Visualization
    st.subheader("📊 BMI Distribution Example")

    sample_data = pd.DataFrame({
        'BMI': np.random.normal(30, 5, 100)
    })

    fig, ax = plt.subplots()
    sns.histplot(sample_data['BMI'], ax=ax)
    ax.set_title("Sample BMI Distribution")

    st.pyplot(fig)