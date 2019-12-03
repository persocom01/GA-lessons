import requests
import time
import pandas as pd

url = 'https://www.reddit.com/r/worldnews.json'
url2 = 'https://www.reddit.com/r/todayilearned/new.json?sort=new'

headers = {'User-agent': 'panzer 2.01'}

r = requests.get(url, headers=headers)
if r.status_code == 200:
    js = r.json()
df = pd.DataFrame([js])
print(df)
