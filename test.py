#!/usr/bin/env python3
import json
import requests
import csv
import os
#import pandas as pd

print('Please enter dates in the format of "YYYY-MM-DD"')

start = input('Enter start date: ')

end = input('Enter end date: ')

deep_link = 'https://api.coindesk.com/v1/bpi/historical/close.json?start={start}&end={end}'.format(start=start, end=end)
response = json.loads(requests.get(deep_link).text)
x = (response['bpi'])
#a = {'2018-01-01': 13412.44, '2018-01-02': 14740.7563, '2018-01-03': 15134.6513}

#os.system('touch /Users/bloom/Desktop/steel/bit_dates.csv')
os.system('touch bit_dates.csv')

# with open('/Users/bloom/Desktop/steel/bit_dates.csv', 'r+') as f:
with open('bit_dates.csv', 'r+') as f:
    dates = csv.writer(f)
    for key, value in x.items():
        dates.writerow([key, value])


# 2018-01-01
# 2018-01-02

print(response['bpi'])
