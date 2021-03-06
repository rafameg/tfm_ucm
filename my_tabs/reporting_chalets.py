import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table as dt
from dash.dependencies import Input, Output
from resources import data_load
import plotly.graph_objects as go
import dash_daq as daq


df_chalets = data_load.data_load_chalets()
numRegistros_df_chalets = df_chalets.shape[0]
precioMaximo_df_chalets = df_chalets['Sale_Price'].max()
precioMinimo_df_chalets = df_chalets['Sale_Price'].min()

valoresVendidos = df_chalets['Sale_Price'].value_counts().values
etiquetasVendidos = df_chalets['Sale_Price'].value_counts().index

valoresCounty = df_chalets['County'].value_counts().values
etiquetasCounty = df_chalets['County'].value_counts().index

valoresYearBuilt = df_chalets['Year_Built'].value_counts().head(20).values
etiquetasYearBuilt = df_chalets['Year_Built'].value_counts().head(20).index


tab_1_layout = html.Div([
					dbc.Row([
						html.H2("Custom Search"),
					]),
					dbc.Row([
			   			dbc.Col(
							html.Div(
								dcc.Dropdown(
									id = 'filter-city-chalets',
									options = [{'label':v, 'value':v} for v in df_chalets.City_Name.unique()],
									value =[],
									multi = True,
									placeholder = "Please select a city"
								)
							), width=3, align='center'
						),
						dbc.Col(
								html.Div(
									dcc.Input(
										id = 'filter-price-chalets',
										placeholder = "Maximum Desired Price",
										style = dict(
										            width = '40%',
										            display = 'table-cell'
										)
									),
								), width=4, align='center'
							)
			   			]),
					html.Hr(),
					dbc.Row([
						html.H2("BI Power Results")
					]),
					dbc.Row([
						dbc.Col([
								dcc.Loading(
									html.Div(
						                id="card-1",
						                children=[
						                    html.P("Number of Closed Sells:"),
						                    daq.LEDDisplay(
						                        id="indicator-ownerships-chalets",
						                        value=numRegistros_df_chalets,
						                        color="#92e0d3",
						                        backgroundColor="#FFFFFF",
						                        size=30,
						                    ),
						                ],
						            ),type='dot'
					            )
		            		]),
						dbc.Col([
								dcc.Loading(
									html.Div(
						                id="card-1",
						                children=[
						                    html.P("Minimum Sale Price:"),
						                    daq.LEDDisplay(
						                        id="indicator-min-price-chalets",
						                        value=precioMinimo_df_chalets,
						                        color="#EF553B",
						                        backgroundColor="#FFFFFF",
						                        size=30,
						                    ),
						                ],
						            ),type='dot'
					            )
		            		]),
						dbc.Col([
								dcc.Loading(
									html.Div(
						                id="card-1",
						                children=[
						                    html.P("Maximum Sale Price:"),
						                    daq.LEDDisplay(
						                        id="indicator-max-price-chalets",
						                        value=precioMaximo_df_chalets,
						                        color="#92e0d3",
						                        backgroundColor="#FFFFFF",
						                        size=30,
						                    ),
						                ],
						            ),type='dot'
					            )
		            		]),
		            ]),
			   		html.Br(),
			   		
			   		dbc.Row([
						dbc.Col(
							html.Div(
								# Y dentro de este DIV es donde incluimos el DataTable
								dt.DataTable(
									id = 'table-chalets',
									columns = [{'name':i, 'id':i} for i in df_chalets.columns],
									data = df_chalets.to_dict('records'), # De esta manera se consigue que se muestren todos
																# los datoss de inicio y luego se vayan filtrando
																# segun se vayan haciendo las selecciones en los Dropdowns
									page_size = 20,
									sort_action = 'native',
									filter_action = 'native',
									style_table = {'overflowX':'scroll', 'overflowY':'scroll', 'maxHeight':'40vh'},
									# style_data_conditional = [
									# 	{
									# 		'if': {
									# 			'row_index': 'odd'
									# 		},
									# 		'backgroundColor': '#EBEBEB'
									# 	}
									# ],
									#style_as_list_view=True,
								    style_cell={'padding': '5px'},
								    style_header={
								        'backgroundColor': 'white',
								        'fontWeight': 'bold'
								    }
									# style_header = {
									# 	'backgroundColor':"#cbddf2",
									# 	'fontWeight':'bod',
									# },
									# style_cell = {
									# 	'padding-left':'2px',
									# 	'textAlign':'left',
									# 	'border':'thin black solid'
									# }
								)
							), width=12, align='center'
						)
					], align = 'end', style = {'padding-top':'2%'}),
					

					dbc.Row([
						dbc.Col(
							html.Div(
								# Y dentro de este DIV es donde se incluye el mapa.
								# Hay que tener en cuenta que un MAPA al final también se considera un GRAFICO,
								# lo unico que el LAYOUT es un poco distinto a un grafico:
								dcc.Graph(
									id = 'map-chalets',
									figure = {
										'data': [
											go.Scattermapbox(
												lat=df_chalets['latitude'],
												lon=df_chalets['longitude'],
												mode='markers',
											)
										],
										'layout': dict(
											title="Neighborhood Dynamic Map",
											autosize = True,
											hovermode = 'closest',
											showlegend = False,
											height = 700,
											mapbox = go.layout.Mapbox(
												accesstoken=open('resources/mapbox_token.txt').read(),
												bearing=0, 
												# Esta es una de las caracteristicas importantes que hay que asignar al grafico,
												# e indica en que coordenadas de latitud y longitud se quiere que empiece el grafico.
												# Se asigna las coordenadas del centro de la ciudad de Miami:
												center=go.layout.mapbox.Center(
													lat = 25.77,
													lon = -80.21
												),
												pitch = 1,
												zoom = 12,
												style = 'light'
											)
										)							

									}

								)

							), width=12, align="center"

						)
					]),
					dbc.Row([
						dbc.Col(
							dcc.Graph(
								id='graph-chalets-sell',
						        figure={
						            'data': [
						                {'x': list(etiquetasVendidos), 'y': list(valoresVendidos), 'type': 'bar'}
						            ],
						            'layout': {
						                'title': 'Closed Sells $'
						            }
						        }
							    
							)
						),
						dbc.Col(
							dcc.Graph(
								id='graph-chalets-county',
						        figure={
						            'data': [
						                {'x': list(etiquetasCounty), 'y': list(valoresCounty), 'type': 'bar'}
						            ],
						            'layout': {
						                'title': 'Sales by County'
						            }
						        }
							    
							)
						),
						dbc.Col(
							dcc.Graph(
								id='graph-chalets-year_built',
						        figure={
						            'data': [
									            go.Pie(
									                labels=list(etiquetasYearBuilt), 
									                values=list(valoresYearBuilt)
									            )
									        ],
						            'layout': {
						                'title': 'Year Built Classification'
						            }
						        }
							    
							)
						)

								
							
					]),
					# Para la interactividad entre los Dropdown y la tabla, hay que
					# añadir un "dcc.Store", para que almacene en un paso intermedio
					# los valores de la tabla para posteriormente mostrarlos en el Dashboard:
					dcc.Store(id = 'intermediate_filter_data_chalets', storage_type = 'memory')

					

			
						
	])












