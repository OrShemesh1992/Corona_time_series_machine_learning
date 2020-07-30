from statsmodels.tsa.ar_model import AutoReg
from random import random
# contrived dataset
data = [x + random() for x in range(1, 100)]
# fit model
model = AutoReg(data, lags=1)
model_fit = model.fit()
print(model)
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat)