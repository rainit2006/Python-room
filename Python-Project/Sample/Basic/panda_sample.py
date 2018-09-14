# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
import requests
url = "http://api.planetos.com/v1/datasets/noaa_gfs_global_sflux_0.12d/point"
#"https://api.planetos.com/v1/datasets/dwd_wam_global/point"
#https://api.planetos.com/v1/datasets/dwd_wam_global/point?origin=dataset-details&lat=49.5&apikey=a959ec00474e460abf64edae3a395f62&lon=-50.5

querystring = {
    "lat":"35.70",   # 緯度
    "lon":"139.80", # 経度,
    "var":"Temperature_surface", # 温度
    "count":"500", # データ取得数
    "apikey":"a959ec00474e460abf64edae3a395f62"  #APIキー
}

response = requests.request( "GET", url, params=querystring)

import json
data = json.loads(response.text)

from pandas.io.json import json_normalize
entry_data = json_normalize( data['entries'] )
#print(entry_data)

import pandas as pd
df = pd.DataFrame( entry_data )
df['axes.time'] = pd.to_datetime(df['axes.time'])

#print(df['data.Temperature_surface'])

i = 0
for temp in df['data.Temperature_surface']:
   temp = temp - 273.15
   df.loc[i, ['data.Temperature_surface']] = temp
   i = i + 1

#print(df.loc[0, ['data.Temperature_surface']])
df.plot( x='axes.time', y='data.Temperature_surface', figsize=(16,4) )

import matplotlib.pyplot as plt
plt.savefig("weather.png")


