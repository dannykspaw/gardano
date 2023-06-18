"""
Author(s): 
    Russell Hedrick; hedrickrussell@gmail.com
    Danny Kearney-Spaw; dannykspaw@gmail.com
Date of Last Revision:  
    06/06/2023
Description:
    Main script to be executed for Garden Project.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                  IMPORTS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import utils
import datetime 
from climate_api.weather_data import WeatherData
# import sensor_programs.rpiFunctions
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

latitude = 30.267
longitude = -97.743
austin_weather = WeatherData(latitude, longitude)
file_name = "gardano_log.csv"
headers = ["Timestamp", "Local Temp", "Local Dew Point", "Local RH", "Status"]
try:
    utils.file_setup(file_name, austin_weather.location, headers)
    
    
except KeyboardInterrupt:
    print("\nProgram terminated as requested.")

except Exception as e:
    print("\nAn unkown error occured at {}:{}. Program terminated.".format(datetime.now().hour, datetime.now().minute))
    print(e)

print(utils.get_time())



