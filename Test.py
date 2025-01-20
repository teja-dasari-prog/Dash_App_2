import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas

app = dash.Dash(__name__)
server=app.server

# Load my data
loaded_data = pd.read_csv('loaded_data.csv')

fig = px.scatter(x='MET-farm', y='farm', data=loaded_data, hue='Month')

if __name__ == "__main__":
    app.run_server(debug=True)

                       
