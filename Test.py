import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
server=app.server

# Load my data
loaded_data = pd.read_csv('loaded_data.csv')

app.layout = html.Div([
    html.H4("Interactive scatter plot with my data"),
    dcc.Graph(id="scatter-plot"),
])

def update_scatter_plot(clickData):
    fig = px.scatter(loaded_data, x='MET-farm', y='farm',title='Scatter Plot Example')
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)

                       
