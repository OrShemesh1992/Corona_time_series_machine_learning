import numpy as np
def mean_absolute_percentage_error(y_true, y_pred):
    return np.mean(np.abs(((y_true - y_pred)+1) / (y_true+1))) * 100
