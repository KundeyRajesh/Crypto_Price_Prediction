import pickle
import esenti_analysis
import yfinance as yf
import pandas as pd
df = yf.download(tickers='ETH-USD')
import numpy as np, pandas as pd, matplotlib.pyplot as plt
import math
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
plt.plot(df.index, df['Adj Close'])

df.tail()
to_row = int(len(df))-10
print(to_row)

training_data = list(df[0:to_row]['Adj Close'])
testing_data = list(df[to_row:]['Adj Close'])
print(training_data[-1],'jkjbk')
plt.figure(figsize=(10,6))
plt.grid(True)
plt.xlabel('Dates')
plt.ylabel('Closing Prices')
plt.plot(df[0:to_row]['Adj Close'], 'green', label='Train')
plt.plot(df[to_row:]['Adj Close'], 'blue', label='Test')
print(df.tail())
model_predictions = []
n_test_obser = len(testing_data)
model=ARIMA(training_data, order = (4,1,0))
model_fit=model.fit()
model_fit.save('emodel.pkl')
print(n_test_obser,'lllolol')
for i in range(n_test_obser):
  print('kkkkkk')
  model = ARIMA(training_data, order = (4,1,0))
  model_fit = model.fit()
  output = model_fit.forecast()
  #yhat = list(output[0])[0]
  model_predictions.append(output)
  actual_test_value = testing_data[i]
  training_data.append(actual_test_value)
mpe=0
mne=0

for i in range(len(model_predictions)):
  if model_predictions[i][0]-testing_data[i]>0:
    mpe+=model_predictions[i][0]-testing_data[i]
  else:
    mne+=model_predictions[i][0]-testing_data[i]
def want_deviat():

  return [mpe/10,mne/10,(mpe+mne)/20]






