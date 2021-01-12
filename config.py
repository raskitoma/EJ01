#############################################
# Ejercicio 1 - config.py
# (c)2021, Elías Achi para todolegal.com
#--------------------------------------------
# App config
#-------------------------------------------- 
# TODO This should run alongside the webcrawler that retrieves data
#-------------------------------------------- 

# Opening librariesconfigparser
import os, sys
import datetime
from flask import Flask

# Initializing
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    APPLICATION_PATH = sys._MEIPASS # pylint: disable=no-member
else:
    APPLICATION_PATH = os.path.dirname(os.path.abspath(__file__))

# Setting up main paths for operation.
UPLOAD_FOLDER = APPLICATION_PATH + '/uploads/'

# Defining allowed extensions
allowed_extensions = {'png'}

# Create the application instance
app = Flask(__name__)

# Extra configs to secure app
# app.config['SECRET_KEY'] = os.urandom(12)
# csrf = CSRFProtect()
# csrf.init_app(app)

# Setting app upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Setting Database Connection URI
# First will look for OS environment variable
# if not it will fallback to SQLite
try:
    DATABASE_CONN = os.environ['DATABASE_URI']
except:
    DATABASE_CONN = None
if ( DATABASE_CONN is None ):
    DATABASE_CONN = 'sqlite:///' + os.path.join(APPLICATION_PATH, 'ejercicio1.db')
app.config['SQLALCHEMY_DATABASE_URI'] =  DATABASE_CONN

# Some usefull functions
def get_timestamp():
    '''
    Just a simple function to retrieve a formatted timestamp.
    '''
    return datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))

def dump_datetime(value):
    '''
    Deserialize datetime object into string form for JSON processing
    '''
    if value is None:
        return None
    return value.strftime("%Y-%m-%d %H:%M:%S")

def twotimes(value):
    if value is None:
        return None
    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

global CRAWLER_URL, CRAWLER_CURR

CRAWLER_URL = 'https://query1.finance.yahoo.com/v7/finance/download/' + \
    '{}=X?' + \
    'period1={}&' \
    'period2={}&' \
    'interval=1d&events=history&includeAdjustedClose=true'

CRAWLER_CURR = ['EURUSD', 'CLPUSD', 'PENUSD']

DWEET_URL = 'https://dweet.io:443/get/latest/dweet/for/thecore'

#WEBHOOK_URL = 'https://webhook.site/176bf904-c2f1-43ff-9314-4a45082569e2' # dev
WEBHOOK_URL = 'https://webhook.site/14693700-0cce-4ef4-9961-e927cf90c008' # Ejercicios

#############################################
# EoF