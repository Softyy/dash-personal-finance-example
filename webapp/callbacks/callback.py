from dash.dependencies import Input,Output

from webapp import app, dm

from datetime import datetime

from ..consts import VENDOR_SELECTOR_ID,OUTPUT_GRAPH_ID,DATE_SELECTOR_ID

from webapp.managers.graph import createFigure,createScatterTrace

@app.callback(
    Output(OUTPUT_GRAPH_ID,'figure'),
    [Input(VENDOR_SELECTOR_ID,'value'),
    Input(DATE_SELECTOR_ID, 'start_date'),
    Input(DATE_SELECTOR_ID, 'end_date')])
def selector_change(selected_values,min_date,max_date):
    x, y = dm.get_selected_charge_series_tuple(selected_values,min_date,max_date)
    return createFigure([createScatterTrace(x,y)])
