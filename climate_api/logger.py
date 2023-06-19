from weather_data import WeatherData
import pandas as pd

latitude = 30.2672
longitude = -97.7431

weather_api = WeatherData(latitude, longitude)
location = weather_api.location
weather_data = weather_api.get_weather()

print(weather_data)

weather_info_store = pd.DataFrame()
weather_info_store['Temperature'] = weather_data[0]
weather_info_store['Dewpoint'] = weather_data[1]
weather_info_store['Relative Humidity'] = weather_data[2]

print(weather_info_store)


