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
    html.H4("Interactive scatter plot with solar farm data"),
    dcc.Graph(id="scatter-plot"),
    html.P("Select Month:"),
    dcc.Dropdown(
        id="Month-dropdown",
        options=[{"label": i, "value": i} for i in loaded_data['Month'].unique()],
        value=loaded_data['Month'].unique()[0]
    )
])

@app.callback(
    Output("scatter-plot", "figure"),
    Input("Month-dropdown", "value")
)

def update_scatter_plot(clickData):
    filtered_loaded_data = loaded_data[loaded_data['Month'] == clickData]
    fig = px.scatter(filtered_loaded_data, x='MET-farm', y='farm', title='Scatter Plot Example', trendline='ols')
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)

                       
