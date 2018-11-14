import plotly.graph_objs as go

def createScatterTrace(x, y, mode='lines+markers', name='unnamed-trace'):
    return go.Scatter(
        x = x,
        y = y,
        mode = mode,
        name = name
    )