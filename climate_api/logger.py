from weather_data import WeatherData
import pandas as pd

"""Specify latitude and logitude"""
latitude = 30.2672
longitude = -97.7431

"""Call weather API"""
weather_api = WeatherData(latitude, longitude)
location = weather_api.location
weather_data = weather_api.get_weather()

"""Store weather API data and future sensor data as a simple dict can just add sensor inputs here """
weather_info = {
'Temperature': [float(weather_data[0])]
,'Dewpoint': [float(weather_data[1])]
,'Relative Humidity': [float(weather_data[2])]
}

weather_info_store = pd.DataFrame.from_dict(weather_info)

weather_info_store.to_csv('../data_aggregation/ambient_data.csv', index=False)


