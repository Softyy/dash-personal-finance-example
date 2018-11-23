# -*- coding: utf-8 -*-
import os
import dash
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

from .templates import index

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.server.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CONNECTION_STRING')
app.server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
db = SQLAlchemy(app.server)

CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.getenv('REDIS_URL'),
    # should be equal to maximum number of users on the app at a single time
    # higher numbers will store more data in the redis cache
    'CACHE_THRESHOLD': 200 
}

cache = Cache()
cache.init_app(app.server, config=CACHE_CONFIG)

# load the data
from .managers.data import DataManager
dm = DataManager()

# check if database is up and running.
import webapp.startup

dm.load_from_db()

x,y = dm.get_charge_series_tuple()

app.layout = index.render(x,y,dm.get_vendor_options())

from .callbacks import callback
