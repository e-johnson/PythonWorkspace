import pandas as pd 
import quandl
import math 
from sklearn import preprocessing, cross_validation, svm 
from sklearn.linear_model import LinearRegression

quandl.ApiConfig.api_key = 'oT_gmV4-4h5DF6rz8NwB' 

df = quandl.get("WIKI/GOOGL")

df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0

df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(value = -99999, inplace = True)
forecast_out = int(math.ceil(0.01 * len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)

df.dropna(inplace=True)