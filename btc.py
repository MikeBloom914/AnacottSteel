#!/usr/bin/env python3
import json
import requests
import csv
import os
#import pandas as pd

print('Please enter dates in the format of "YYYY-MM-DD"')

start = input('Enter start date: ')

end = input('Enter end date: ')

# try:
#     os.remove(bit_dates.csv)
# except OSError:
#     pass

deep_link = 'https://api.coindesk.com/v1/bpi/historical/close.json?start={start}&end={end}'.format(start=start, end=end)
response = json.loads(requests.get(deep_link).text)
#x = (response['bpi'])
x = response([])
os.system('touch bit_dates.csv')

with open('bit_dates.csv', 'r+') as f:
    dates = csv.writer(f)
    for key, value in x.items():
        dates.writerow([key, value])
