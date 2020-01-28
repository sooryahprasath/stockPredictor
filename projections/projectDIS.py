#Install the dependencies
import quandl
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import datetime
from assets import config, tickers

ticker = tickers.ticker_DIS
#Get the stock data
df = quandl.get(ticker, api_key=config.key)
#Plot a intial graph
#df.Close.plot()
#plt.show()

df = df[['Close']]
