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

#make the api call

#get city names and station names

stations_total = pd.DataFrame()
stations_df = pd.DataFrame()
x = 0
while x < 20000:
    r = requests.get('https://www.ncei.noaa.gov/cdo-web/api/v2/stations?offset={}&limit=1000'.format(x), headers={'token':token})
    d = json.loads(r.text)
    stations_df = pd.json_normalize(d['results'])
    stations_total = pd.concat([stations_total, stations_df])
    print(stations_total.tail())
    print(x)
    x = x + 1000

stations_total.to_csv('api_information/city_data.csv')

print(stations_total)

