import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output



tab_1_layout = dbc.Container([
					dcc.Tabs(id="tabs-analysis", value='Description', children=[
				        dcc.Tab(label='Analyze Flats', value='AnalisisPisos'),
				        dcc.Tab(label='Analyze Chalets', value='AnalisisChalets'),
				    ]),
				    dbc.Row([
						html.Div([
									html.H2("Analysis"),
									html.P("Extract useful information from data and taking the decision based upon the data analysis.")
								])
					]),
					html.Hr(),
					html.Div(id='tabs-content-analysis')

				], fluid = True)







