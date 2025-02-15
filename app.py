import streamlit as st
import requests

# User input for parameters
st.markdown('## Ride Parameters')

# Date input
ride_date = st.date_input("Select date of the ride")

# Time input
ride_time = st.time_input("Select time of the ride")

# Combine date and time into one datetime object
from datetime import datetime

ride_datetime = datetime.combine(ride_date, ride_time)

pickup_long = st.number_input("Pickup longtitude", format="%.6f")
pickup_lat = st.number_input("Pickup latitude", format="%.6f")
dropff_long = st.number_input("Dropoff Longitude", format="%.6f")
dropoff_lat = st.number_input("Dropoff Latitude", format="%.6f")

passenger_count = st.slider("Passenger Count", 1, 6, 1)

url = 'https://taxifare.lewagon.ai/predict'

params = {
    "pickup_datetime": ride_datetime.isoformat(),
    "pickup_longitude": pickup_long,
    "pickup_latitude": pickup_lat,
    "dropoff_longitude": dropff_long,
    "dropoff_latitude": dropoff_lat,
    "passenger_count": passenger_count
}

if st.button("get fare prediction"):
    st.markdown('sending request to the API...')

    response = requests.get(url, params=params)

    prediction = response.json()

    if response.status_code == 200:
        st.markdown(f"### Estimated Fare: ${prediction['fare']:.2f}")

    else:
        st.error("There was an issue retrieving the prediction. Please try again")
        st.write(prediction)
