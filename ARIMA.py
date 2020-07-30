
#ARIMA - autoregressive integrated moving average 

# Importing the libraries
import numpy as np 
import pandas as pd 
import matplotlib.pylot as plt 
from statsmodels.tsa.seasonal import seasonal_decompose 
from parser import init_start

#read and choose country from corona file
init_start()
# airline = pd.read_csv('AirPassengers.csv', 
#                        index_col ='Month', 
#                        parse_dates = True) 
  
# # Print the first five rows of the dataset 
# airline.head() 
  
# # ETS Decomposition 
# result = seasonal_decompose(airline['# Passengers'],  
#                             model ='multiplicative') 
  
# # ETS plot  
# result.plot() 

  
# # Import the library 
# from pmdarima import auto_arima 
  
# # Ignore harmless warnings 
# import warnings 
# warnings.filterwarnings("ignore") 
  
# # Fit auto_arima function to AirPassengers dataset 
# stepwise_fit = auto_arima(airline['# Passengers'], start_p = 1, start_q = 1, 
#                           max_p = 3, max_q = 3, m = 12, 
#                           start_P = 0, seasonal = True, 
#                           d = None, D = 1, trace = True, 
#                           error_action ='ignore',   # we don't want to know if an order does not work 
#                           suppress_warnings = True,  # we don't want convergence warnings 
#                           stepwise = True)           # set to stepwise 
  
# # To print the summary 
# stepwise_fit.summary() 


# # Split data into train / test sets 
# train = airline.iloc[:len(airline)-12] 
# test = airline.iloc[len(airline)-12:] # set one year(12 months) for testing 
  
# # Fit a SARIMAX(0, 1, 1)x(2, 1, 1, 12) on the training set 
# from statsmodels.tsa.statespace.sarimax import SARIMAX 
  
# model = SARIMAX(train['# Passengers'],  
#                 order = (0, 1, 1),  
#                 seasonal_order =(2, 1, 1, 12)) 
  
# result = model.fit() 
# result.summary() 



# start = len(train) 
# end = len(train) + len(test) - 1
  
# # Predictions for one-year against the test set 
# predictions = result.predict(start, end, 
#                              typ = 'levels').rename("Predictions") 
  
# # plot predictions and actual values 
# predictions.plot(legend = True) 
# test['# Passengers'].plot(legend = True) 



# # Load specific evaluation tools 
# from sklearn.metrics import mean_squared_error 
# from statsmodels.tools.eval_measures import rmse 
  
# # Calculate root mean squared error 
# rmse(test["# Passengers"], predictions) 
  
# # Calculate mean squared error 
# mean_squared_error(test["# Passengers"], predictions) 



# # Train the model on the full dataset 
# model = model = SARIMAX(airline['# Passengers'],  
#                         order = (0, 1, 1),  
#                         seasonal_order =(2, 1, 1, 12)) 
# result = model.fit() 
  
# # Forecast for the next 3 years 
# forecast = result.predict(start = len(airline),  
#                           end = (len(airline)-1) + 3 * 12,  
#                           typ = 'levels').rename('Forecast') 
  
# # Plot the forecast values 
# airline['# Passengers'].plot(figsize = (12, 5), legend = True) 
# forecast.plot(legend = True) 