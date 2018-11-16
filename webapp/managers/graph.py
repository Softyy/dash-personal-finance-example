import plotly.graph_objs as go

from ..consts import WEBAPP_GRAPH_TITLE

def createScatterTrace(x, y, mode='lines+markers', name='unnamed-trace'):
    return go.Scatter(
        x = x,
        y = y,
        mode = mode,
        name = name
    )

def createFigure(data,layout={'title': WEBAPP_GRAPH_TITLE}):
    return {'data': data,'layout': layout}