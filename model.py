#!/usr/bin/env python3

import json
import sqlite3
import time
import requests
import os


def stock(stock):
    deep_link = 'https://www.quandl.com/api/v3/datasets/WIKI/{stock}.json?start_date={start}&end_date={end}'.format(stock=stock, start=start, end=end)
    response = json.loads(requests.get(deep_link).text)
    whole = (response['dataset'])
    # may have to change WIKI to EOD
    # https://www.quandl.com/api/v3/datasets/EOD/{stock}.json?start_date=2018-04-09&end_date=2018-04-11&api_key=ZxbbrDjmsCg4vFZC1Uu5

    a = []
    x = [[k, v] for k, v in whole.items()]
    y = x[17][1]x
    for i in y:
        key = (i[0])
        value = (i[4])
        a.append((key, value))

    sort_list = sorted(a)
    # print(sort_list)
    b = dict(sort_list)
    print(b)
