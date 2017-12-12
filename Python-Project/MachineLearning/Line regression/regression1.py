# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 17:30:39 2017

@author: svf14n29
"""

import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot')

quandl.ApiConfig.api_key = 'vyumwDhy-jf4kgiziZ_p'
df = quandl.get_table('WIKI/PRICES', ticker='GOOGL')
df.set_index('date', inplace=True)

df = df[['adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_volume']]
df['HL_PCT'] = (df['adj_high'] - df['adj_close'])/df['adj_close'] * 100.0
df['PCT_change'] = (df['adj_close'] - df['adj_open'])/df['adj_open'] * 100.0
  
df = df[['adj_close', 'HL_PCT', 'PCT_change', 'adj_volume']]

forecast_col = 'adj_close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))
print(forecast_out)
df['label'] = df[forecast_col].shift(-forecast_out)

#print(df.head())

X = np.array(df.drop(['label'], 1))
#print(X)
X = preprocessing.scale(X)
#print(X)
X_lately = X[-forecast_out:]
#print(X_lately)
X = X[:-forecast_out]
#print(X)
df.dropna(inplace=True)
y = np.array(df['label'])
#print(y)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
#print(X_train)
#print(X_test)
#print(y_train)
#print(y_test)

#for k in ['linear','poly','rbf','sigmoid']:
#    clf = svm.SVR(kernel = k)
#    #clf = LinearRegression()
#    clf.fit(X_train, y_train)
#    confidence = clf.score(X_test, y_test)
#    print(k, confidence)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)

forecast_set = clf.predict(X_lately)

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]

plt.figure(figsize=(15,10))

df = df.tail(500)
df['adj_close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()