# Moving Average (MA)

# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import warnings
from parser import init_start
from score import mean_absolute_percentage_error

#read and choose country from corona file
init_start()
corona = pd.read_csv('dataset/chosenCountry.csv')

# Ignore harmless warnings
warnings.filterwarnings("ignore")

# dt=datetime.datetime.strptime(date, '%m/%d/%y').strftime('20%y-%m-%d')
corona.Day = pd.to_datetime(corona.Day,format='%m/%d/%y')
corona.index = corona.Day

# Split data into train / test sets
train = corona.iloc[:len(corona)-45]
test = corona.iloc[len(corona)-45:] # set 45 day for testing

# Create prediction table
y_hat = test.copy()

# Create Moving Average from last 60 periods
y_hat['Forecast'] = train['deaths_confirmed'].rolling(60).mean().iloc[-1]

#mean absolute percentage error
print("mean absolute percentage error: " , mean_absolute_percentage_error(test.deaths_confirmed, y_hat.Forecast),"%")

#Plotting data
plt.figure(figsize=(12,8))
plt.plot(test.index,test['deaths_confirmed'], label='test-prediction')
plt.plot(train.index, train['deaths_confirmed'], label='train-deaths_confirmed')
plt.plot(y_hat.index,y_hat['Forecast'], label='MA-Forecast')
plt.legend(loc='best')
plt.title("Moving Average (MA) Forecast")
plt.xlabel('Days')
plt.ylabel('deaths_confirmed')
plt.show()
