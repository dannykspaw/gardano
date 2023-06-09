import requests
import pandas as pd
import json
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# Specify the URL of the token request page
url = "https://www.ncei.noaa.gov/cdo-web/api/v2/datasets"

token = "HGecygnRwvZitOoPhfCpuQmMgMhsnZhF"
temps = []
prcp = []
year = "2023"
location_id = "CITY:US480005"

#make the api call, sort of overkill calling three times at once---will readjust
avg_temps_for_city = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=TAVG&limit=1000&locationid={}&startdate='.format(location_id)+year+'-01-01&enddate='+year+'-12-31', headers={'token':token})
avg_precipitation = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=PRCP&limit=1000&locationid={}&startdate='.format(location_id)+year+'-01-01&enddate='+year+'-12-31', headers={'token':token})
avg_sunshine = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=TSUN&limit=1000&locationid={}&startdate='.format(location_id)+year+'-01-01&enddate='+year+'-12-31', headers={'token':token})

available_datatypes = requests.get('https://api.weather.gov/points/30.2672,97.7431')

# /observations/2023-06-12T17:42:13Z/hourly

#modify r based on whatever variables need above, I put a few above out of curiousity to see what they have to offer
r = available_datatypes
print(r)

#load the api response as a json then convert it to pandas DF
d = json.loads(r.text)
print(d)
web_response_df = pd.json_normalize(d)
web_response_df = web_response_df.to_string()
print(web_response_df)

#basically just built a conditional statement to do the logic I am supposed to do here (i.e. get temp data)
if r == avg_temps_for_city:
    avg_temps = [item for item in d['results'] if item['datatype']=='TAVG']
    #get the date field from all average temperature readings
    dates_temp = [item['date'] for item in avg_temps]
    #get the actual average temperature from all average temperature readings
    temps = [item['value'] for item in avg_temps]

    #initialize dataframe
    df_temp = pd.DataFrame()

    #populate date and average temperature fields (cast string date to datetime and convert temperature from tenths of Celsius to Fahrenheit)
    df_temp['date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_temp]
    df_temp['avgTemp'] = [float(v)/10.0*1.8 + 32 for v in temps]

    #print results and plots
    print(df_temp)
    df_temp.plot('date','avgTemp')
    plt.show()

else:
    None
