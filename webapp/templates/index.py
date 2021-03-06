import dash_core_components as dcc
import dash_html_components as html

from ..managers.graph import createScatterTrace,createFigure

from ..consts import WEBAPP_TITLE,WEBAPP_SUBTITLE,MIN_DATE_SELECTOR,MAX_DATE_SELECTOR,VENDOR_TEST_OPTIONS,VENDOR_SELECTOR_ID,OUTPUT_GRAPH_ID,DATE_SELECTOR_ID

def render(x,y,vendor_options=VENDOR_TEST_OPTIONS):
    return html.Div(children=[
        html.H1(children=WEBAPP_TITLE),

        html.H5(children=WEBAPP_SUBTITLE),

        dcc.DatePickerRange(
            id=DATE_SELECTOR_ID,
            minimum_nights=7,
            clearable=True,
            with_portal=True,
            min_date_allowed=MIN_DATE_SELECTOR,
            start_date=MIN_DATE_SELECTOR,
            max_date_allowed=MAX_DATE_SELECTOR,
            end_date=MAX_DATE_SELECTOR
        ),

        dcc.Dropdown(
            id=VENDOR_SELECTOR_ID,
            options=vendor_options,
            multi=True,
            value=[vendor_options[0]['value']]
        ),

        dcc.Graph(
            id=OUTPUT_GRAPH_ID,
            figure=createFigure([createScatterTrace(x,y)])
        )
    ])