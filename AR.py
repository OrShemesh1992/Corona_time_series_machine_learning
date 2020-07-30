# Autoregression (AR)

# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import warnings
from parser import init_start
from statsmodels.tsa.ar_model import AR

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

#create prediction table
model = AR(train.deaths_confirmed)
fit1 = model.fit()
y_hat = test.copy()
# Forecast for the next 30 Days
y_hat['Forecast'] = fit1.predict(start=len(train), end=len(train)+len(test)-1 + 30, dynamic=False)

#Plotting data
plt.figure(figsize=(12,8))
plt.plot(test.index,test['deaths_confirmed'], label='test-prediction')
plt.plot(train.index, train['deaths_confirmed'], label='train-deaths_confirmed')
plt.plot(y_hat.index,y_hat['Forecast'], label='AR-Forecast')
plt.legend(loc='best')
plt.title("Autoregression (AR) Forecast")
plt.xlabel('Days')
plt.ylabel('deaths_confirmed')
plt.show()
