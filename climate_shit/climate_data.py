import requests
import pandas as pd
import json
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# Specify the URL of the token request page
url = "https://www.ncei.noaa.gov/cdo-web/api/v2/datasets"

# Get the token request form
response = requests.get(url, headers={})

token = "HGecygnRwvZitOoPhfCpuQmMgMhsnZhF"

dates_temp = []
dates_prcp = []
temps = []
prcp = []
year = "2023"

#make the api call
r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=TAVG&limit=1000&stationid=CITY:US480005&startdate='+year+'-01-01&enddate='+year+'-12-31', headers={'token':token})

#load the api response as a json
d = json.loads(r.text)
#get all items in the response which are average temperature readings
print(d)
avg_temps = [item for item in d['results'] if item['datatype']=='TAVG']
print(avg_temps)
#get the date field from all average temperature readings
dates_temp = [item['date'] for item in avg_temps]
#get the actual average temperature from all average temperature readings
temps = [item['value'] for item in avg_temps]

#initialize dataframe
df_temp = pd.DataFrame()

#populate date and average temperature fields (cast string date to datetime and convert temperature from tenths of Celsius to Fahrenheit)
df_temp['date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_temp]
df_temp['avgTemp'] = [float(v)/10.0*1.8 + 32 for v in temps]

print(df_temp)
df_temp.plot('date','avgTemp')
plt.show()
