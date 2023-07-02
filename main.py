"""
Author(s): 
    Russell Hedrick; hedrickrussell@gmail.com
    Danny Kearney-Spaw; dannykspaw@gmail.com
Date of Last Revision:  
    07/01/2023
Description:
    Main script to be executed for Garden Project. Script is designed to be 
    executed with a cronjob (crontab -e to add job on rpi).
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                  IMPORTS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import utils
import time
from datetime import datetime
from climate_api.weather_data import WeatherData
import sensor_programs.rpiFunctions as rpi
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pump1 = 17 # Basil and Mint
pump2 = 18 # Tomatoes
hour_count = 0
latitude = 30.2672
longitude = -97.7431
austin_weather = WeatherData(latitude, longitude)
file_location = "/home/pi/Documents/Sams_Farm/gardano/"
file_name = file_location + "gardano_log.csv"
headers = ["Timestamp", "Local Temp", "Local Dew Point", "Local RH", "Soil Temp", "Soil Moisture", "Status"]
try:
    utils.file_setup(file_name, austin_weather.location, headers)
    
    # Run pumps in 30 second intervals
    rpi.pump_control(pump1, 30)
    rpi.pump_control(pump2, 30)
    rpi.pump_control(pump1, 30)
    rpi.pump_control(pump2, 30)
    rpi.pump_control(pump1, 30)
    rpi.pump_control(pump2, 30)
    rpi.pump_control(pump1, 30)
    rpi.pump_control(pump2, 30)

    soil_temp = rpi.vegetronix_temp(0)
    soil_moist = rpi.vegetronix_moist(3)

    timestamp = str(utils.get_time())
    data = list(austin_weather.get_weather())
    data.insert(0, timestamp)
    data.insert(4, soil_temp)
    data.insert(5, soil_moist)
    print(data)
    utils.write_data(data, file_name)
    
except Exception as e:
    error = ["An unkown error occured at {}:{}. Program terminated.".format(datetime.now().hour, datetime.now().minute)]
    print(e)
    utils.write_data(error, file_name)




