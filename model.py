#!/usr/bin/env python3

import json
import sqlite3
import time
import requests
import os


def dates(start_date, end_date):

    deep_link = 'https://api.coindesk.com/v1/bpi/historical/close.json?start={start_date} & end={end_date}'.format(start=start_date, end=end_date)
    response = json.loads(requests.get(deep_link).text)

    connection = sqlite3.connect('master.db', check_same_thread=False)
    cursor = connection.cursor()

    start_date = response['start']
    end_date = response['end']

    cursor.execute('SELECT balance FROM users;')
    balance = cursor.fetchall()[0][0]
    unix_time = time.time()
