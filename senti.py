import pickle
import numpy as np
import json
import requests
import pandas as pd
api_url = "https://api.senticrypt.com/v1/bitcoin.json"
data = requests.get(api_url).json()
print(data[0])
print(data[0]['rate'])
rate1=data[0]['rate']
median1=data[0]['median']
count1=data[0]['count']

sum1=data[0]['sum']
last1=data[0]['last']
mean1=data[0]['mean']

print([rate1,median1,count1,sum1,last1,mean1])
def sent_req():
    return [rate1,median1,count1,sum1,last1,mean1]


