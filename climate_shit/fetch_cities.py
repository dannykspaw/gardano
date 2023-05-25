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
r = requests.get("https://www.ncei.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CITY&sortfield=name&sortorder=desc", headers={'token':token})

#load the api response as a json
d = json.loads(r.text)
print(d['results'])
#get city names and station names
for x in range(10):
    name = [item for item in d['results']['name']]
    station_id = [item for item in d['results']['id']]
    print(name)
    print(station_id)

#initialize dataframe
stations_df = pd.DataFrame()

stations_df['name'] = name
stations_df['station_id'] = station_id

print(stations_df)

# print(df_temp)
# df_temp.plot('date','avgTemp')
# plt.show()
