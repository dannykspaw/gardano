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
dataframe = pd.json_normalize(d['results'])
print(dataframe)

stations_df = pd.DataFrame()
stations_df['name'] = dataframe['name']
