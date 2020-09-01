import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import my_callbacks
import dash_app


#app = dash.Dash()

if __name__ == '__main__':
    dash_app.app.run_server(host='0.0.0.0',port='8080',debug=True)