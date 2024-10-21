import streamlit as st
import joblib

rfc = joblib.load('model.joblib')
st.title("Car System Predictive Maintenance Classification")

col1, col2 = st.columns(2)

with col1:
    selected_type = st.selectbox('Select a Type', ['Low', 'Medium', 'High'])
    type_mapping = {'Low': 0, 'Medium': 1, 'High': 2}
    selected_type = type_mapping[selected_type]
  
with col2:
    frequency = st.text_input('Frequency (Hz)')

with col1:
    pressure = st.text_input('Pressure (Bar)')

with col2:
    rotational_speed = st.text_input('Rotational speed [rpm]')

with col1:
    gear = st.text_input('Gear (No)')

with col2:
    voltage = st.text_input('Voltage (V)')

# code for Prediction
failure_pred = ''

# creating a button for Prediction
if st.button('Predict Failure'):
    failure_pred = rfc.predict([[selected_type,frequency, 
                                 pressure,rotational_speed,
                                 gear,voltage]])
    
    if (failure_pred[0] == 1):
        failure_pred = 'Failure'
    else:
        failure_pred = 'No Failure'
    
st.success(failure_pred)