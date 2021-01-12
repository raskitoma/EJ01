#############################################
# Ejercicio 1 - ejercicio2.py
# (c)2021, Elías Achi para todolegal.com
#--------------------------------------------
# ejercicio 2
#-------------------------------------------- 
# TODO This should use sched library to better perform the task
# TODO Right now is sleeping each (x) seconds just to give a functional test
#-------------------------------------------- 

# Opening libraries
import requests
import time
from config import DWEET_URL, WEBHOOK_URL
from util import push_webhook

def dweet_request(my_url):
    response = requests.get(DWEET_URL).json()
    try:
        data_required = response['with'][0]['content']
        my_temp = data_required['temperature']
        my_humi = data_required['humidity']
        push_webhook('http://localhost:6969/Core/', data = {'Temp' : my_temp, 'Humidity' : my_humi})

    except ValueError:
        return False

def dweet_store():
    response = requests.get('http://localhost:6969/Core/')
    push_webhook(WEBHOOK_URL, response)

if __name__ == '__main__':
    master_looper = 0
    while True:
        master_looper += 1
        dweet_request(DWEET_URL)
        time.sleep(60)
        if (master_looper % 15 == 0):
            master_looper = 0
            dweet_store()








#############################################
# EoF