#!/usr/bin/env python3
import json
import requests


print('Please enter dates in the format of "YYYY-MM-DD"')

start = input('Enter start date: ')

end = input('Enter end date: ')

deep_link = 'https://api.coindesk.com/v1/bpi/historical/close.json?start={start}&end={end}'.format(start=start, end=end)
response = json.loads(requests.get(deep_link).text)

print(response['bpi'])
