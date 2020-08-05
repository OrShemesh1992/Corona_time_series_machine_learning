# Covid-19 & Time Series



## Authors

Snir Shaharabani 

Or Shemesh 



![image](https://user-images.githubusercontent.com/46107190/88951370-8ec28580-d29e-11ea-9561-8143eaac6934.png)




## About the project:


This project includes three Time series algorithms:

* Autoregression (RA)
* Moving Averages (MA)
* Seasonal Autoregressive Integrated Moving Average (SARIMA)


The dataset we have chosen to use:

* The number of deaths from all countries on different dates (until 22/7/20)
* The amount of those infected from each country on different dates (until 22/7/20)


After transferring the data to a limited table of date and number of deaths or infections per country, 
we used the three algorithms to predict the next 30 days in that country.

The user can select a country and parameter sick or dead and the models will do theirs.





## conclusion:


After examining data from the State of Israel, 
we found that there would be an increase in the number of dead and infected in the next 30 days

After checking the correctness of the models we can say that the MA model is the most accurate of the three.



### Autoregression

Mean absolute percentage error of deaths in Israel:  47.01799474850447%

Mean absolute percentage error of Confirmed case in Israel : 65.2883985198%

![image](https://user-images.githubusercontent.com/46107190/88950906-f6c49c00-d29d-11ea-873a-2e647340c6e7.png)

![image](https://user-images.githubusercontent.com/46107190/88950922-fcba7d00-d29d-11ea-94c9-0019c2754505.png)


**************


### Moving Averages

Mean absolute percentage error of deaths in Israel:  95.30899470899472 %

Mean absolute percentage error of Confirmed case in Israel : 64.1830211770 %


![image](https://user-images.githubusercontent.com/46107190/88950937-0217c780-d29e-11ea-91ca-da9a9ff121d1.png)

![image](https://user-images.githubusercontent.com/46107190/88950952-08a63f00-d29e-11ea-8657-a5407ad751ca.png)



**************



### SARIMA

Mean absolute percentage error of deaths in Israel:  64.26148397024254%

Mean absolute percentage error of Confirmed case in Israel : 76.5041482159%


![image](https://user-images.githubusercontent.com/46107190/88950974-0f34b680-d29e-11ea-8f48-0dbabdcf9b72.png)

![image](https://user-images.githubusercontent.com/46107190/88950993-152a9780-d29e-11ea-865f-fb4f17346e85.png)





## Sources:

* https://www.kaggle.com/ 

* https://www.geeksforgeeks.org/python-arima-model-for-time-series-forecasting

* https://github.com/advaitsave/Introduction-to-Time-Series-forecasting-Python/blob/master/Time%20Series%20in%20Python.ipynb

* https://www.rdocumentation.org/packages/forecast/versions/8.12/topics/auto.arima

* https://www.statsmodels.org/dev/examples/notebooks/generated/statespace_sarimax_stata.html

* https://github.com/tristanga/Machine-Learning/tree/master/Time%20Series%20Forecasting
