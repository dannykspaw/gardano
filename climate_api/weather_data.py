import requests
import pandas as pd
import json
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# Specify the URL of the token request page

# Set the latitude and longitude coordinates for your desired location
latitude = 30.2672
longitude = -97.7431

# Retrieve the grid endpoint using the /points endpoint
points_url = f"https://api.weather.gov/points/{latitude},{longitude}"
response = requests.get(points_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    forecast_url = data["properties"]["forecast"]
    # Retrieve the forecast data using the grid endpoint
    forecast_response = requests.get(forecast_url)
#    print(forecast_response)
    if forecast_response.status_code == 200:
        forecast_data = forecast_response.json()
        print(forecast_data)
        # Parse the forecast data and extract the desired weather information
    else:
        print("Forecast request failed with status code:", forecast_response.status_code)
else:
    print("Points request failed with status code:", response.status_code)
