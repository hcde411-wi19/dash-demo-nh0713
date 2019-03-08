# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash(__name__, static_folder='static')
df = pd.read_csv('static/data_car_2004.csv')
app.layout = html.Div(children=[

    html.H1(children='Scatter Plot'),

    html.Div(children='''
        Shows that price increases with Horsepower
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                go.Scatter(
                    x=df['HP'],
                    y=df['Retail Price'],
                    mode='markers',
                    text=df['Vehicle Name'],
                    marker={
                        'size': 10,
                        'opacity': 0.8
                    }
                )
            ],
            'layout': {
                'title': 'Car Dataset 2004',
                'xaxis': {'title': 'Horse Power'},
                'yaxis': {'title': 'Retail Price'},
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)