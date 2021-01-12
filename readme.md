# Ejercicio TL

Part 1: Simple test of backend api that crawls for data on site and stores to DB. Then sents results(on demand) to an specified webhook

Part 2: Requests and grab data from IoT related site using their API each 60 seconds, stores data and after 15 minutes queries the DB and push data to webhook

***
Part 2 could be improved, i.e. using sched library instead of simple time.sleep(n) function (n is seconds)

Also instead of using python this could be migrated to other platforms for faster development, like simple javascript.
***

## Usage

- Part 1 must run [main.py](main.py), then browse to http://localhost:6969 use the following entrypoints:
  - Crawler (Get): to perform a crawling operation. Must set currency(string) possible values for now are: EURUSD, CLPUSD and PENUSD. This will returns a successfull/error response. If successfull it will store last 5 days of data(will not duplicate values if already present on DB)

  - Data (Get): to retrieve last 5 days of stored data.  Mus set currency(string) possible values for now are: EURUSD, CLPUSD and PENUSD. This will return a json object with data of last 5 days and at the same time will push the same data to the configured Webhook on [config.py](config.py). If no data is retrieved, will return a No Data error msg

- Part 2 must run script [ejercicio2.py](ejercicio2.py).  This script depends on [main.py](main.py) to be running.  This is configured to query dweet.io each 60 seconds to store data to db and also each 15 minutes it will push the last 15 entries to the webhook configured in [config.py](config.py)
