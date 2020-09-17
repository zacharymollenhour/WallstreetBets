import numpy as np
import os
import pandas as pd
from iexfinance.stocks import Stock
from datetime import datetime
import matplotlib.pyplot as plt
from iexfinance.stocks import get_historical_data
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split


Stock.IEX_TOKEN = 'pk_04da3e6c36334468ac1513b3adfe1531'
basepath = 'https://cloud.iexapis.com/stable/stock/'
basepath2 = '/chat/date/20200101?token=pk_04da3e6c36334468ac1513b3adfe1531'
delta = get_historical_data('DAL', start, end, output_format='pandas')
delta.drop(["open","high","low"], axis=1, inplace=True)

print(delta.plot())