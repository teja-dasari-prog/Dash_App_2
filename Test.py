import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)

# Sample data
df = px.data.gapminder()

# App layout
app.layout = html.Div([
    html.H1("Dropdown Example"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['country'].unique()],
        value='Canada'  # Default value
    ),
    dcc.Graph(id='life-expectancy-graph')
])

# Callback to update graph based on dropdown selection
@app.callback(
    Output('life-expectancy-graph', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(filtered_df, x='year', y='lifeExp', title=f'Life Expectancy in {selected_country}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
