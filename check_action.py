#!/usr/bin/python3

import sys
import ast
import json
import smtplib
import os.path
import requests
import datetime

weekday = int(datetime.date.today().weekday())
hour = int(datetime.datetime.now().strftime("%H"))
if weekday >= 5 and hour < 9 or hour > 17:
    exit()

configFile = "config.json"

if os.path.exists(configFile) == False:
    sys.exit("Configuration file does not exist.")

with open(configFile, encoding='utf-8') as file:
    config = json.load(file)

for user in config['users']:
    for action in user['actions']:
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + action['label'] + ".SA&outputsize=compact&apikey=" + config['token_api']
        r = requests.get(url)
        data = r.json()
        today = datetime.date.today()
        close = ast.literal_eval("{:.2f}".format(ast.literal_eval(data['Time Series (Daily)'][today]['4. close'])))

        message = ''
        if (action['purchase'] is not None):
            if (close <= action['purchase']):
                message = user['first_name'] + " it's time for purchase action " + action['label'] + " for " + data['Time Series (Daily)']['2022-03-11']['4. close'] + "."

        if (action['sell'] is not None):
            if (close >= action['sell']):
                message = user['first_name'] + " it's time for sell action " + action['label'] + " for " + data['Time Series (Daily)']['2022-03-11']['4. close'] + "."

        if (message != ''):
            sender = 'Stock monitoring service <servico@monitor.com.br>'
            receiver = user['first_name'] + ' ' + user['last_name'] + ' <' + user['email'] + '>'
            message = f"""\
Subject: Alert of stock monitoring service
To: {receiver}
From: {sender}

""" + message
            with smtplib.SMTP(config['email']['server'], config['email']['port']) as srv:
                srv.login(config['email']['username'], config['email']['password'])
                srv.sendmail(sender, receiver, message)