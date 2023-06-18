import requests
import pandas as pd
import json
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt


class WeatherData:
    """
    The following WeatherData class allows users to specify a latitude and 
    longitude in order to retrieve location, and weather data.
    This program uses the NOAA National Weather Service API.
    """
    def __init__(self, latitude, longitude):
        # Retrieve the grid endpoint using the /points endpoint
        # Specify the URL of the token request page
        points_url = f"https://api.weather.gov/points/{latitude},{longitude}"
        response = requests.get(points_url)
        if response.status_code == 200:
            data = response.json()
            formatted_data = json.dumps(data, indent=4)
            city = data['properties']['relativeLocation']['properties']['city']
            state = data['properties']['relativeLocation']['properties']['state']
            self.location = city+', '+state
            self.weather_url = data['properties']['forecastHourly']
        else:
            print("Points request failed with status code:", response.status_code)
            self.location = None
            self.weather_url = None

        self.latitude = latitude
        self.longitude = longitude

    def get_weather(self):
        response = requests.get(self.weather_url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            formatted_data = json.dumps(data, indent=4) # only used for viewing
            temp = data['properties']['periods'][0]['temperature']
            dewpoint = data['properties']['periods'][0]['dewpoint']['value']*1.8 + 32
            rh = data['properties']['periods'][0]['relativeHumidity']['value']
            return temp, round(dewpoint,1), rh
        else:
            print("Points request failed with status code:", response.status_code)
            return None, None, None

    def get_temp(self):
        response = requests.get(self.weather_url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            formatted_data = json.dumps(data, indent=4)
            temp = data['properties']['periods'][0]['temperature']
            return temp
        else:
            print("Points request failed with status code:", response.status_code)
            return None
         
            

if __name__ == "__main__":
    
    # EXAMPLE
    # Set the latitude and longitude coordinates for your desired location
    latitude = 30.2672
    longitude = -97.7431
    
    weather = WeatherData(latitude, longitude)
    location = weather.location
    weather_data = weather.get_weather()

    temp = weather_data[0]
    print(temp)

    lat = input("User input latitude:\n")
    long = input("User input longitude:\n")

    random_weather = WeatherData(lat, long)
    random_location = random_weather.location
    random_temp = random_weather.get_weather()[0]
    print(f"""
    The specified location is: {random_location}
    Temperature: {random_temp}""")

