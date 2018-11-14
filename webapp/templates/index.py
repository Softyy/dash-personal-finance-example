import dash_core_components as dcc
import dash_html_components as html

from ..managers.graph import createScatterTrace

from ..consts import WEBAPP_TITLE, WEBAPP_SUBTITLE, WEBAPP_GRAPH_TITLE

def render(x,y):
    return html.Div(children=[
        html.H1(children=WEBAPP_TITLE),

        html.H5(children=WEBAPP_SUBTITLE),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    createScatterTrace(x,y)
                ],
                'layout': {
                    'title': WEBAPP_GRAPH_TITLE
                }
            }
        )
    ])