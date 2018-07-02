#!/usr/bin/env python3

import time
from flask import Flask, redirect, render_template, request, url_for
import model


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        email = request.form['email']
        password = request.form['password']

        if email != 'mikebloom914@gmail.com' or password != 'swordfish':
            return render_template('index.html', message='BAD CREDENTIALS...Please try again')
        else:
            return redirect(url_for('homepage'))


@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template('homepage.html')
    else:
        return render_template('homepage.html')


@app.route('/stock', methods=['GET', 'POST'])
def stocks():
    if request.method == 'GET':
        return render_template('stock.html')
    else:
        start_date = request.form['start']
        end_date = request.form['end']
        x = model.stock(stock)
        return render_template('stock.html', message=x)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
