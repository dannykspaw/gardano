import requests
import pandas as pd
import json
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# Specify the URL of the token request page
token = "HGecygnRwvZitOoPhfCpuQmMgMhsnZhF"
year = "2023"

#make the api call, sort of overkill calling three times at once---will readjust

available_data_sets = requests.get('https://www.ncei.noaa.gov/cdo-web/api/v2/locations?limit=1000', headers={'token':token})

#modify r based on whatever variables need above, I put a few above out of curiousity to see what they have to offer
r = available_data_sets
#load the api response as a json then convert it to pandas DF
d = json.loads(r.text)
web_response_df = pd.json_normalize(d['results'])
web_response_df = web_response_df.to_string()

print(web_response_df)
