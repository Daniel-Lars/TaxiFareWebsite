import streamlit as st
from datetime import datetime, date
import pandas as pd
import pytz
import requests
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:

- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''
# date parameter input

today_date = date.today()
now = datetime.now()

d = st.date_input("Select your pick up date", today_date)
st.write(d)
# time parameter input

t = st.time_input('Select your pick up time', now)
#datetime.time(8, 45)
# pick up and drop off input
st.write(t)

pickup_longitude = st.number_input('Enter your pickup longitude', 40.7614327)
pickup_latitude = st.number_input('Enter your pickup latitude', -73.9798156)
dropoff_longitude = st.number_input('Enter your dropoff longitude', 40.6413111)
dropoff_latitude = st.number_input('Enter your dropoff latitude', -73.9797156)

### drop down box for passenger count

drop_down_slection = [1,2,3,4,5,6,7,8]

passenger_count = st.selectbox('Select passenger count', drop_down_slection)


# - - - - - - - -



url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown(
        'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
    )
'''

2. Let's build a dictionary containing the parameters for our API...


3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

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
st.write(request)
