#!/usr/bin/env python3
import json
import requests
import csv
import os
import quandl
#import pandas as pd

stock = input('Please enter stock symbol you want to compare:  ')
stock = stock.upper()

print('Please enter dates in the format of "YYYY-MM-DD"')

start = input('Enter start date: ')

end = input('Enter end date: ')

# try:
#     os.remove(bit_dates.csv)
# except OSError:
#     pass
api_key = 'ZxbbrDjmsCg4vFZC1Uu5'

deep_link = 'https://www.quandl.com/api/v3/datasets/WIKI/{stock}.json?start_date={start}&end_date={end}&api_key={api_key}'.format(stock=stock, start=start, end=end, api_key=api_key)
response = json.loads(requests.get(deep_link).text)

# data = quandl.get_table('WIKI/PRICES', qopts={'columns': ['ticker', 'date', 'close']}, ticker=['AAPL', 'MSFT'], date={'gte': '2016-01-01', 'lte': '2016-12-31'})

# print(response)

#x = response([dataset])
x = response(['dataset'])
os.system('touch stock.csv')

with open('stock.csv', 'r+') as f:
    dates = csv.writer(f)
    for key, value in x.items():
        dates.writerow([key, value])
