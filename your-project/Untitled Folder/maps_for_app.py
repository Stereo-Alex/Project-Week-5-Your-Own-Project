import os
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.express as px

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server


# Load Data


data1 = pd.read_csv("Data_project/data11.csv", sep=';' )
# Build App
app.layout = html.Div([
    dcc.RadioItems(
        id="radio2",
        options=[
            {"label": "Happiness Score", "value": "Happiness Score"},
            {"label": "GDP_per_capita", "value": "GDP_per_capita"},
            {"label": "Overall rank", "value": "Overall rank"},
            
        ],
        value = "Happiness Score"
    ),
    dcc.Graph(id="choropleth"),
])
# Define callback to update graph
@app.callback(
    Output('choropleth', 'figure'),
    [Input("radio2", "value")]
)
def update_figure(y):
    fig = px.choropleth(data1, locations="Country",
                     locationmode="country names",
                    color=y, 
                    hover_name="Country",
                    
                    projection="orthographic",
                    color_continuous_scale="RdBu",
                    
                   )

    return  fig
    
# Run app and display result inline in the notebook
if __name__ == '__main__':
    app.run_server(debug=True)
