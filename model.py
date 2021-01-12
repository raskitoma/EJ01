#############################################
# Ejercicio 1 - model.py
# (c)2021, Elías Achi para todolegal.com
#--------------------------------------------
# DB Models
#-------------------------------------------- 
# TODO
#-------------------------------------------- 

# Opening libraries
from flask_sqlalchemy import SQLAlchemy
from config import app, dump_datetime

db = SQLAlchemy(app)

class Currencies_Log(db.Model):
    __tablename__ = 'currencies_log'
    id = db.Column('id', db.Integer, primary_key = True)
    log_time = db.Column('log_time', db.DateTime, nullable = False)
    log_curr = db.Column('log_curr', db.Text, nullable = False)
    log_val = db.Column('log_val', db.Float, nullable = False)

    def __init__(self, id, log_time, log_curr, log_val):
        self.id = id
        self.log_time = log_time
        self.log_curr = log_curr
        self.log_val = log_val
    
    def __repr__(self):
        return f'id={self.id}, log_time={dump_datetime(self.log_time)}, \
            log_curr={self.log_curr}, log_val={self.log_val}'

    @property
    def serialize(self):
        return {
            'id'        : self.id,
            'log_time'  : dump_datetime(self.log_time),
            'log_curr'  : self.log_curr,
            'log_val'   : self.log_val
        }

class TheCore(db.Model):
    __tablename__ = 'thecore'
    id = db.Column('id', db.Integer, primary_key = True)
    core_temp = db.Column('core_temp', db.Float, nullable = False)
    core_humi = db.Column('core_humi', db.Float, nullable = False)

    def __init__(self, id, core_temp, core_humi):
        self.id = id
        self.core_temp = core_temp
        self.core_humi = core_humi
    
    def __repr__(self):
        return f'id={self.id}, core_temp={self.core_temp}, core_humi={self.core_humi}'

    @property
    def serialize(self):
        return {
            'id'        : self.id,
            'core_temp' : self.core_temp,
            'core_humi' : self.core_humi
        }


# Call db creation
db.create_all()

#############################################
# EoF