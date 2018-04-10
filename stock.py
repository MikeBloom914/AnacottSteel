#!/usr/bin/env python3
import json
import requests
import csv
import os
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

deep_link = 'https://www.quandl.com/api/v3/datasets/WIKI/{stock}.json?start_date={start}&end_date={end}'.format(stock=stock, start=start, end=end)
response = json.loads(requests.get(deep_link).text)

print(response)

# x = (response['bpi'])

# os.system('touch bit_dates.csv')

# with open('bit_dates.csv', 'r+') as f:
#     dates = csv.writer(f)
#     for key, value in x.items():
#         dates.writerow([key, value])
