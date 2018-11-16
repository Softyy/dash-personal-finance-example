from dash.dependencies import Input,Output

from webapp import app, dm

from ..consts import VENDOR_SELECTOR_ID,OUTPUT_GRAPH_ID

from webapp.managers.graph import createFigure,createScatterTrace

@app.callback(
    Output(OUTPUT_GRAPH_ID,'figure'),
    [Input(VENDOR_SELECTOR_ID,'value')])
def selector_change(selected_values):
    x, y = dm.get_selected_charge_series_tuple(selected_values)
    return createFigure([createScatterTrace(x,y)])