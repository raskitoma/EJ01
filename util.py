#############################################
# Ejercicio 1 - util.py
# (c)2021, Elías Achi para todolegal.com
#--------------------------------------------
# Utilities library
#-------------------------------------------- 
# TODO
#-------------------------------------------- 

# Opening libraries
import time
import math
import requests
import json
from flask import request, jsonify
from datetime import datetime, timedelta
from config import CRAWLER_CURR, CRAWLER_URL, WEBHOOK_URL
from model import db, Currencies_Log, TheCore

def dt_to_unix():
    print('hola')

def date_current():
    return datetime.today()

def date_previous(start_date, days):
    return start_date - timedelta(days=days)

def date_2_unix(my_date):
    return math.trunc(time.mktime(my_date.timetuple()))

def unix_2_date(my_date):
    return datetime.utcfromtimestamp(int(my_date))

def query_url_maker(url, currency, period1, period2):
    return url.format(currency,date_2_unix(period1), date_2_unix(period2))

def crawler(currency, url):
    date_to = date_current()
    date_from = date_previous(date_to, 6)
    data_request = requests.get(query_url_maker(url, currency, date_from, date_to ))
    data_content = data_request.text
    processed_lines = 0
    for line in data_content.split('\n'):
        data = line.split(',')
        try:
            val_exch = float(data[4])
            val_date = datetime.strptime( data[0], '%Y-%m-%d')
            processed_lines += 1
            create_curr(currency, val_date, val_exch)
        except ValueError:
            continue

    return {'Response' : 'Processed {} lines!'.format(processed_lines)}

def query_curr(currency, my_date):
    if (my_date is None):
        log_vector = Currencies_Log.query.filter(Currencies_Log.log_curr == currency).all()
        if log_vector is not None:
            response = jsonify(json_list = [i.serialize for i in log_vector]).json
            return response['json_list']
        else:
            return False        
    else:
        log_vector = Currencies_Log.query.filter((Currencies_Log.log_curr == currency) & (Currencies_Log.log_time == my_date)).first()
        if log_vector is not None:
            return log_vector
        else:
            return False        
    
def create_curr(currency, my_date, my_val):
    log_vector = query_curr(currency, my_date)
    if (log_vector is False):
        new_currency_data = Currencies_Log(None, my_date, currency, my_val)
        db.session.add(new_currency_data)
        db.session.commit()
        return True
    else:
        return False

def push_webhook(WebhookURL, data):
    response = requests.post(WebhookURL, data = data)
    return response

class Currency_UPD(object):
    def curr_list(self):
        qry_curr = request.args.get('currency')
        response = query_curr(qry_curr, None)
        if (response == False):
            return { 'Response' : 'No data available!' }
        push_webhook(WEBHOOK_URL, response[0])
        return response

    def curr_crawler(self):
        my_curr = request.args.get('currency')
        response = crawler(my_curr, CRAWLER_URL)
        return response

class CoreMan(object):
    def list(self):
        core_vector = TheCore.query.order_by(TheCore.id.desc()).limit(15).all()
        if core_vector is not None:
            response = jsonify(json_list = [i.serialize for i in core_vector]).json
            return response['json_list']
        else:
            return False
    
    def insert(self):
        my_temp = request.form.get('Temp')
        my_humidity = request.form.get('Humidity')
        new_core = TheCore(None, my_temp, my_humidity)
        db.session.add(new_core)
        try:
            db.session.commit()
            return True
        except ValueError:
            return False

        
#############################################
# EoF