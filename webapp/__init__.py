# -*- coding: utf-8 -*-
import dash

from .managers.data import DataManager

from .templates import index

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# load the data
dm = DataManager()
dm.load_data()
x,y = dm.get_charge_series_tuple()
vendor_options = dm.get_vendor_options()

app.layout = index.render(x,y,vendor_options)