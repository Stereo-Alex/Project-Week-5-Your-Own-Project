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


data1 = pd.read_csv("data11.csv", sep=';' )
data_2 = pd.read_csv("animation.csv")


app.layout = html.Div([
    dcc.RadioItems(
        id="radio",
        options=[
            {"label": "Social support", "value": "Social support"},
            {"label": "Healthy life expectancy", "value": "Healthy life expectancy"},
            {"label": "Freedom to make life choices", "value": "Freedom to make life choices"},
            {"label": "Generosity", "value": "Generosity"},
            {"label": "Perceptions of corruption", "value": "Perceptions of corruption"},
            {"label": "GDP_per_capita", "value": "GDP_per_capita"}

        ],
        value = "Social support"
    ),
    dcc.Graph(id="scatter"),

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

    dcc.Graph(id="animation"), 
    dcc.Dropdown(id="mydropdown")])



@app.callback(
        Output("scatter", "figure"), 
        [Input("radio", "value")])


def scatter(x):
    fig3 = px.scatter(data1, x = data1["Happiness Score"], y=x, color=data1["continent"],
                 hover_data=["Country"], title=f"Interactive Scatter plot with comparing {x} and Happiness")

        # we also update the marker line 
    fig3.update_layout({
                        "plot_bgcolor": "rgba(0, 0, 0, 0)",
                        "paper_bgcolor": "rgba(0, 0, 0, 0)"})
    fig3.update_traces(marker=dict(size=8, line=dict(width=1.5,
                                        color='DarkSlateGrey')))

    return fig3

@app.callback(
        Output('choropleth', 'figure'),
        [Input("radio2", "value")])

def choropleth(y):
    fig = px.choropleth(data1, locations=data1["Country"],
                     locationmode="country names",
                    color=y, 
                    hover_name=data1["Country"],
                    
                    projection="orthographic",
                    color_continuous_scale="RdBu",
                    title=f"Interactive Globe with respect to {y}"
                    
                   )

    return  fig


@app.callback(
            Output("animation", "figure"), 
            [Input("mydropdown", "value")])
 


def animation(Human_Fredom_Index):
    fig4 = px.scatter(data_2, x=data_2["Regualtions on business index"], y=data_2["Human_Fredom_Index"], 
          animation_frame=data_2.year[::-1],
          animation_group = "countries",
          color="region", hover_name="countries",
          log_x=True, title=f"Interactive Animation of Business index and Human Freedom")

    fig4.update_layout({
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)"})
    fig4.update_traces(marker=dict(size=8, line=dict(width=1.5,
                                        color='DarkSlateGrey')))

    return fig4



if __name__ == '__main__':
    app.run_server(debug=True)
