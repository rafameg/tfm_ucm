import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output



tab_1_layout = dbc.Container([
					dcc.Tabs(id="tabs-reporting", value='ReportingChalets', children=[
				        dcc.Tab(label='Reporting Flats', value='ReportingPisos'),
				        dcc.Tab(label='Reporting Chalets', value='ReportingChalets'),
				    ]),
				    dbc.Row([
						html.Div([
									html.H2("Reporting"),
									html.P("Business intelligence reporting, or BI reporting, is the process of gathering data by utilizing different software and tools to extract relevant insights. Ultimately, it provides suggestions and observations about business trends, empowering decision-makers to act.")
								])
					]),
					html.Hr(),
					html.Div(id='tabs-content-reporting')

				], fluid = True)







