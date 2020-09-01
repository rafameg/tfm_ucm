import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import my_callbacks

external_stylesheets = [dbc.themes.SPACELAB]

app = dash.Dash(__name__,external_stylesheets=external_stylesheets,title="Real Estate Prediction")
server = app.server

app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([
							    html.H1('Real Estate Prediction Platform'),
							    dcc.Tabs(id="tabs-master", value='Description', 
							    	children=[
								        dcc.Tab(label='Introduction', value='Introduction'),
								        dcc.Tab(label='Gallery', value='gallery'),
								        dcc.Tab(label='Reporting', value='Reporting'),
								        dcc.Tab(label='Analysis', value='Analysis')
							    ]),
							    html.Div(id='tabs-content-master')
							])