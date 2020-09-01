import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import base64


test_png_rafa = 'resources/team_images/image_rafa.png'
test_base64_rafa = base64.b64encode(open(test_png_rafa, 'rb').read()).decode('ascii')

test_png_jorge = 'resources/team_images/image_jorge.jpeg'
test_base64_jorge = base64.b64encode(open(test_png_jorge, 'rb').read()).decode('ascii')

test_png_ruben = 'resources/team_images/image_ruben.jpeg'
test_base64_ruben = base64.b64encode(open(test_png_ruben, 'rb').read()).decode('ascii')

test_png_miguel = 'resources/team_images/image_miguel.jpeg'
test_base64_miguel = base64.b64encode(open(test_png_miguel, 'rb').read()).decode('ascii')

test_png_arturo = 'resources/team_images/image_arturo.jpeg'
test_base64_arturo = base64.b64encode(open(test_png_arturo, 'rb').read()).decode('ascii')

test_png_javier = 'resources/team_images/image_javier.jpg'
test_base64_javier = base64.b64encode(open(test_png_javier, 'rb').read()).decode('ascii')

tab_1_layout = html.Div([
			    	
			    	
					dbc.Container([
						dbc.Row([
								html.Br(),
								html.H2('Welcome'),
								html.Div([
										html.P('The current website consists of the final project of the Big Data and Business Analytics master''s degree at the UCM, in which a web tool is developed for the prediction of real state housing prices for the state of Florida, United States. The work has been carried out by a multidisciplinary team of six people, who have jointly carried out the different parts of it.')
									]),

								#html.Iframe(src = 'https://player.vimeo.com/video/254172349'),
								# html.P("Percentage of accomplishment is: "),
								# html.Div([
								#         dbc.Progress("50%", value=50,  style={"height": "30px", "width":"1000px"})
								# ])
							]),
						html.Div([
						html.Hr(),
						dbc.Row([
								html.H2('Project Structure'),
								html.Br(),
								html.Hr()
								
							]),
						]),

						dbc.Row([
							html.P("The different parts of which the project is made up are the following:")
							]),
						dbc.Row([
								html.Div([
										dbc.Button('Data Extraction',id = 'collapse-button-data-extraction',className = 'mb-3',color = 'secondary'),
			                       			dbc.Collapse(dbc.Card(dbc.CardBody('Process that involves retrieval of data from various sources, in our case, we extract the data from real state agency')),id = 'collapse-data-extraction', is_open=True),
			                       		dbc.Button('Data Cleaning',id = 'collapse-button-data-cleaning',className = 'mb-3',color = 'secondary'),
			                       			dbc.Collapse(dbc.Card(dbc.CardBody('Process of detecting and correcting (or removing) corrupt or inaccurate records from a record set, table, or database and refers to identifying incomplete, incorrect, inaccurate or irrelevant parts of the data and then replacing, modifying, or deleting the dirty or coarse data')),id = 'collapse-data-cleaning', is_open=True),
			                       		dbc.Button('Data Analysis',id = 'collapse-button-data-analysis',className = 'mb-3',color = 'secondary'),
			                       			dbc.Collapse(dbc.Card(dbc.CardBody('Process of inspecting, cleansing, transforming and modeling data with the goal of discovering useful information, informing conclusions and supporting decision-making')),id = 'collapse-data-analysis', is_open=True),
			                       		dbc.Button('Modelization',id = 'collapse-button-modelization',className = 'mb-3',color = 'secondary'),
			                       			dbc.Collapse(dbc.Card(dbc.CardBody('Displaying data in a digestible and approachable way')),id = 'collapse-modelization', is_open=True),
			                       		dbc.Button('Reporting',id = 'collapse-button-reporting',className = 'mb-3',color = 'secondary'),
			                       			dbc.Collapse(dbc.Card(dbc.CardBody('This content is hidden in the collapse')),id = 'collapse-reporting', is_open=True),
			                       		dbc.Button('Web',id = 'collapse-button-web',className = 'mb-3',color = 'secondary'),
			                       			dbc.Collapse(dbc.Card(dbc.CardBody('Building portable app for using all the previous sections')),id = 'collapse-web', is_open=True)
                       				])

										# dbc.Toast(
										#     [html.P("Process that involves retrieval of data from various sources, in our case, we extract the data from real state agency", className="mb-0")],
										#     header="Data Extraction",
										# ),
										# dbc.Toast(
										#     [html.P("process of detecting and correcting (or removing) corrupt or inaccurate records from a record set, table, or database and refers to identifying incomplete, incorrect, inaccurate or irrelevant parts of the data and then replacing, modifying, or deleting the dirty or coarse data", className="mb-0")],
										#     header="Data Cleaning",
										# ),
										# dbc.Toast(
										#     [html.P("Process of inspecting, cleansing, transforming and modeling data with the goal of discovering useful information, informing conclusions and supporting decision-making", className="mb-0")],
										#     header="Data Analysis",
										# ),
										# dbc.Toast(
										#     [html.P("This is the content of the toast", className="mb-0")],
										#     header="Modelization",
										# ),
										# dbc.Toast(
										#     [html.P("This is the content of the toast", className="mb-0")],
										#     header="Reporting",
										# ),
										# dbc.Toast(
										#     [html.P("This is the content of the toast", className="mb-0")],
										#     header="Web",
										# )
										# dbc.ListGroup([
										# 	        dbc.ListGroupItem("Extract, transform and load", color="primary"),
										# 	        dbc.ListGroupItem("Data Cleaning", color="secondary"),
										# 	        dbc.ListGroupItem("Data Analysis", color="success"),
										# 	        dbc.ListGroupItem("Modelization", color="warning"),
										# 	        dbc.ListGroupItem("Reporting", color="danger"),
										# 	        dbc.ListGroupItem("Web", color="info"),
										# 	    ])
										#])
																
							],justify="center", align="center", className="h-50"),
						
						html.Hr(),
						dbc.Row([
							html.H2("About us"),
						]),
						dbc.Row([
							html.P("We are a group of six people with different profiles: engineering, science, law, statistics, finance: ")
						]),
						dbc.Row([
							
							dbc.Col(
								dbc.Card(
									    	[	
										        dbc.CardImg(src='data:image/png;base64,{}'.format(test_base64_ruben), top=False),
										        dbc.CardBody(
										            [
										                html.H5("Rubén Basadre", className="card-title"),
										                dbc.Button("Learn more", href="https://www.linkedin.com/in/rubén-basadre-423255169" , color="primary"),
										            ]
										        ),
									    	],
									    style={"width": "18rem"},
										)
								),
							dbc.Col(
								dbc.Card(
									    	[	
										        dbc.CardImg(src='data:image/png;base64,{}'.format(test_base64_rafa), top=False),
										        dbc.CardBody(
										            [
										                html.H5("Rafael Megales", className="card-title"),
										                dbc.Button("Learn more", href="https://www.linkedin.com/in/rmegales" , color="primary"),
										            ]
										        ),
									    	],
									    style={"width": "18rem"},
										)
								),
							dbc.Col(
								dbc.Card(
									    	[	
										        dbc.CardImg(src='data:image/png;base64,{}'.format(test_base64_jorge), top=False),
										        dbc.CardBody(
										            [
										                html.H5("Jorge Muñoz", className="card-title"),
										                dbc.Button("Learn more", href="https://www.linkedin.com/in/jmunozmendoza" , color="primary"),
										            ]
										        ),
									    	],
									    style={"width": "18rem"},
										)
								)

						]),
						dbc.Row([

							dbc.Col(
								dbc.Card(
									    	[	
										        dbc.CardImg(src='data:image/png;base64,{}'.format(test_base64_javier), top=False),
										        dbc.CardBody(
										            [
										                html.H5("Javier Alonso", className="card-title"),
										                dbc.Button("Learn more", href="https://www.linkedin.com/in/javier-alonso-4b85383a" , color="primary"),
										            ]
										        ),
									    	],
									    style={"width": "18rem"},
										)
								),
							dbc.Col(
								dbc.Card(
									    	[	
										        dbc.CardImg(src='data:image/png;base64,{}'.format(test_base64_rafa), top=False),
										        dbc.CardBody(
										            [
										                html.H5("Arturo Lopez", className="card-title"),
										                dbc.Button("Learn more", href="https://www.linkedin.com/in/arturo-lópez-iglesias-0b9b991b4" , color="primary"),
										            ]
										        ),
									    	],
									    style={"width": "18rem"},
										)
								),
							dbc.Col(
								dbc.Card(
									    	[	
										        dbc.CardImg(src='data:image/png;base64,{}'.format(test_base64_miguel), top=False),
										        dbc.CardBody(
										            [
										                html.H5("Miguel Molina", className="card-title"),
										                dbc.Button("Learn more", href="https://www.linkedin.com/in/miguel-ángel-molina-2354b3192" , color="primary"),
										            ]
										        ),
									    	],
									    style={"width": "18rem"},
										)
								)

						])


					])
			       
			   		
])

