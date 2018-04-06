#!/usr/bin/env python3
import json
import requests
import csv
import os
import pandas as pd

print('Please enter dates in the format of "YYYY-MM-DD"')

start = input('Enter start date: ')

end = input('Enter end date: ')

deep_link = 'https://api.coindesk.com/v1/bpi/historical/close.json?start={start}&end={end}'.format(start=start, end=end)
response = json.loads(requests.get(deep_link).text)
print(response['bpi'])

#os.system('touch /Users/bloom/Desktop/steel/BitcoinDates.csv')

# with open('/Users/bloom/Desktop/steel/BitcoinDates.csv', 'r+') as d:
#writer = csv.writer(d)
#    for key, value in dates:
#        d.writerow(key, value)

# d.close()
#
# 2018-01-01
# 2018-02-02

# print(response['bpi'])
