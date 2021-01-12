#############################################
# Ejercicio 1 - master.py
# (c)2021, Elías Achi para todolegal.com
#--------------------------------------------
# Master api endpoint file
#-------------------------------------------- 
# TODO
#-------------------------------------------- 

# Opening libraries
from flask_restx import Api, Resource, reqparse
from requests.api import request
from werkzeug.middleware.proxy_fix import ProxyFix
from config import app, CRAWLER_CURR
from util import Currency_UPD, CoreMan

# Creating api
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api (
    app,
    title = 'Currency-Crawler-API',
    version = '0.0.1 alpha',
    description = 'Backend to craw for currency, store data and request'
)

# Namespaces (just to order)
ns1 = api.namespace('Crawler', description = 'Crawler Operation')
ns2 = api.namespace('Data', description = 'Data operations')
ns3 = api.namespace('Core', description = 'TheCore data handler')

# Parser objects
query_data_parser = reqparse.RequestParser()
query_data_parser.add_argument('currency', help = 'Currency Request', location = 'query', \
    choices = CRAWLER_CURR, required = True)

core_store = reqparse.RequestParser()
core_store.add_argument('Temp', help = 'Core Temp', location = 'form', required = True)
core_store.add_argument('Humidity', help = 'Core Humidity', location = 'form', required = True)

@ns1.route('/')
class Data_Request(Resource):
    @ns1.expect(query_data_parser)
    def get(self):
        return Currency_UPD.curr_crawler(self), {'Access-Control-Allow-Origin': '*'}


@ns2.route('/')
class Data_Request(Resource):
    @ns2.expect(query_data_parser)
    def get(self):
        return Currency_UPD.curr_list(self)

@ns3.route('/')        
class Data_Core(Resource):
    def get(self):
        return CoreMan.list(self), {'Access-Control-Allow-Origin': '*'}
    @ns3.expect(core_store)
    def post(self):
        return CoreMan.insert(self), {'Access-Control-Allow-Origin': '*'}

### Main app!!!
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)

#############################################
# EoF