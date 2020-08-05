
#SARIMA - Seasonal Autoregressive Integrated Moving-Average

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.seasonal import seasonal_decompose
from parser import init_start
from pmdarima import auto_arima
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from statsmodels.tools.eval_measures import rmse
from score import mean_absolute_percentage_error

#read and choose country from corona file
init_start()
corona = pd.read_csv('dataset/chosenCountry.csv')

# Ignore harmless warnings
warnings.filterwarnings("ignore")

# Fit auto_arima function to corona dataset
stepwise_fit = auto_arima(corona['deaths_confirmed'], start_p = 1, start_q = 1,
                          max_p = 3, max_q = 3, m = 12,
                          start_P = 0, seasonal = True,
                          d = None, D = 1, trace = False,
                          error_action ='ignore',   # we don't want to know if an order does not work
                          suppress_warnings = True,  # we don't want convergence warnings
                          stepwise = True)           # set to stepwise

# Split data into train / test sets
train = corona.iloc[:len(corona)-45]
test = corona.iloc[len(corona)-45:] # set 45 day for testing

# Fit a SARIMAX(0, 1, 1)x(2, 1, 1, 12) for Seasonal model on the training set
model = SARIMAX(train['deaths_confirmed'],
                order = (0, 1, 1),
                seasonal_order =(2, 1, 1, 12))

# Fitting ARIMA to the Training set
result = model.fit()

# Predictions for 45 days against the test set
predictions = result.predict(len(train), len(train) + len(test) - 1,
                             typ = 'levels').rename("Predictions")

#mean absolute percentage error
print("mean absolute percentage error: " , mean_absolute_percentage_error(test["deaths_confirmed"], predictions),"%")

# plot predictions
predictions.plot(legend = True)

# Train the model on the full dataset
model = model = SARIMAX(corona['deaths_confirmed'],
                        order = (0, 1, 1),
                        seasonal_order =(2, 1, 1, 12))
result = model.fit()

# Forecast for the next 30 Days
forecast = result.predict(start = len(corona),
                          end = (len(corona)-1) + 30,
                          typ = 'levels').rename('Forecast')


# Plot the forecast values
corona['deaths_confirmed'].plot(figsize = (30, 5), legend = True)
forecast.plot(legend = True)
plt.title('SARIMA - Seasonal Autoregressive Integrated Moving-Average')
plt.xlabel('Days')
plt.ylabel('deaths_confirmed')
plt.show()
