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
r = requests.get("https://www.ncei.noaa.gov/cdo-web/api/v2/stations", headers={'token':token})

#load the api response as a json
d = json.loads(r.text)
print(d)
#get city names and station names
stations_df = pd.json_normalize(d['metadata'])
stations_df = stations_df[stations_df['name'].str.contains("Austin, TX")].sort_values('name', ascending=0)
austin_id = stations_df['id']
print(austin_id)