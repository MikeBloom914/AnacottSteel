#!/usr/bin/env python3
import json
import requests
import csv
import os
# import pandas as pd

# stock = input('Please enter stock symbol you want to compare:  ')
# stock = stock.upper()

# print('Please enter dates in the format of "YYYY-MM-DD"')

# start = input('Enter start date: ')

# end = input('Enter end date: ')

# try:
#     os.remove(bit_dates.csv)
# except OSError:
#     pass


deep_link = 'https://www.quandl.com/api/v3/datasets/WIKI/AAPL.json?&start_date=2018-01-01&end_date=2018-01-08&api_key=ZxbbrDjmsCg4vFZC1Uu5'

response = json.loads(requests.get(deep_link).text)
whole = (response['dataset'])
# print(whole)

a = []
x = [[k, v] for k, v in whole.items()]
y = x[17][1]
# z = y[0]
for i in y:
    key = (i[0])
    value = (i[4])
    a.append((key, value))

sort_list = sorted(a)
print(sort_list)
b = dict(sort_list)
print(b)
# print(c)
# print(d)
# ZxbbrDjmsCg4vFZC1Uu5.  my key so I can keep requesting from quandl

# os.system('touch stock.csv')

# with open('stock.csv', 'r+') as f:
#     dates=csv.writer(f)
#     for key, value in c.items():
#         dates.writerow([key, value])
