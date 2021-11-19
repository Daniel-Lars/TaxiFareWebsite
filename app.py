import streamlit as st
from datetime import datetime, date
import pandas as pd
import pytz
import requests
import numpy as np


import folium

import os

import pandas as pd

'''
# TaxiFareModel
'''

# date parameter input

today_date = date.today()
now = datetime.now()

d = st.date_input("Select your pick up date", today_date)
# time parameter input

t = st.time_input('Select your pick up time', now)

# pick up and drop off input

pickup_longitude = st.number_input('Enter your pickup longitude', -73.13)
pickup_latitude = st.number_input('Enter your pickup latitude', 40.76)
dropoff_longitude = st.number_input('Enter your dropoff longitude', -73.13)
dropoff_latitude = st.number_input('Enter your dropoff latitude', 40.64 )

### drop down box for passenger count

drop_down_slection = [1,2,3,4,5,6,7,8]

passenger_count = st.selectbox('Select passenger count', drop_down_slection)


# - - - - - - - -



url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown(
        'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
    )


# request dictionary containing the request parameters

pickup_datetime = str(d) + ' ' + str(t)


pickup_datetime = datetime.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")
eastern = pytz.timezone("US/Eastern")
localized_pickup_datetime = eastern.localize(pickup_datetime, is_dst=None)
utc_pickup_datetime = localized_pickup_datetime.astimezone(pytz.utc)
formatted_pickup_datetime = utc_pickup_datetime.strftime(
    "%Y-%m-%d %H:%M:%S UTC")

formatted_pickup_datetime = str(d) + ' ' + str(t)


params = dict(pickup_datetime=formatted_pickup_datetime,
              pickup_longitude=pickup_longitude,
              pickup_latitude=pickup_latitude,
              dropoff_longitude=dropoff_longitude,
              dropoff_latitude=dropoff_latitude,
              passenger_count=passenger_count
              )


url = 'https://taxifare.lewagon.ai/predict'

request = requests.get(url, params=params).json()
request = request.get('prediction','no prediciton available')

if st.button('Predict'):
    st.write(round(request,2))

else:
    st.write('⬆️ Click me 🙌🏼🎈')


# Map creation

m = folium.Map(location=[40.78, -73.96], zoom_start=9)

folium.Marker(
    location=[pickup_latitude, pickup_longitude],
    #popup=city.city,
    icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(m)

folium.Marker(
    location=[dropoff_latitude, dropoff_longitude],
    #popup=city.city,
    icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(m)

folium_static(m)
