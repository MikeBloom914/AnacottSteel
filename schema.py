#!/usr/bin/env python3

import sqlite3


connection = sqlite3.connect('master.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        email VARCHAR,
        password VARCHAR
    );"""
)

cursor.execute(
    """CREATE TABLE dates(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        start_date VARCHAR(10),
        end_date VARCHAR(10)
    );"""
)

cursor.close()
connection.close()
