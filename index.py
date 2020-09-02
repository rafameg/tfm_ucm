from app import app
import dash_html_components as html
import dash_core_components as dcc
import my_callbacks
from app import server

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

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port='8080',debug=True)