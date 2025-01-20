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

fig = px.scatter(loaded_data, x='MET-farm', y='farm', color='Month',title='Scatter Plot Example')

if __name__ == "__main__":
    app.run_server(debug=True)

                       
