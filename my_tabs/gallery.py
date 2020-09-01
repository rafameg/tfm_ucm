import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from resources import data_load

df_chalets = data_load.data_load_images_chalets()

tab_1_layout = dbc.Container([
    html.Hr(),
    # Se Crea la PRIMERA FILA:
    dbc.Row([
        # La primera fila solo incluye UNA COLUMNA, esta columna
        # contiene el titulo de esta seccion:
        dbc.Col(
            html.Div([
                html.H2('Chalets Image Gallery'),
            ],style = {'text-align' : 'left'} ),
            width={'offset' : 4}
            )
    ]),
    html.Hr(),  # Añade un linea horizontal

    # Se Crea la SEGUNDA FILA:
    dbc.Row([
        # Solo contiene un columna que incluye un elemento
        # MARKDOWN, que sera una pequeña descripcion de la seccion:
        dbc.Col(
            html.Div([
                dcc.Markdown(
                    id = 'markdown',
                    children = '''
                        In this section you can see images of chalets in some of the most important cities in the state of **Florida**, taking into account some characteristic as a *garden* or *pool*.
                    '''
                )
            ]),
            
            ),
        ]),
    dbc.Row([
        dbc.Col(
            html.Div([
                html.Iframe(src = 'https://player.vimeo.com/video/254172349?autoplay=1',  style={'width': 700, 'height' : 400, 'horizontal-align': 'center'})
            ],style = {'text-align' : 'left'} ),
            width={'offset' : 2}
            )
        ]),

    
    html.Hr(),  # Añade un linea horizontal

    # Se Crea la TERCERA FILA:
    dbc.Row([
        # PRIMERA COLUMNA de la tercera fila, esta columna contiene el elemento de alarma
        # que lo usamos para resaltar el texto de encabezado del RadioItem de ciudades: 
        dbc.Col(
            html.Div([
                dbc.Alert([
                    "Select city:", 
                ], color = 'dark')
            ]), width = {'size':2, 'offset':2}, align = 'center'
           
        ),
        # SEGUNDA COLUMNA de la tercera fila, esta columna contiene el elemento de alarma
        # que lo usamos para resaltar el texto de encabezado del RadioItem de caracteristicas: 
        dbc.Col(
            html.Div([
                dbc.Alert([
                    "Select features:", 
                ], color = 'dark')
            ]), width = {'size':2, 'offset':4}, align = 'center'
        )
    ]),


    # Se Crea la CUARTA FILA:
    dbc.Row([
        # PRIMERA COLUMNA de la cuarta fila, esta columna contiene
        # el elemento RadioItem para seleccionar una ciudad: 
        dbc.Col(
            html.Div([
                dcc.RadioItems(
                    id='city',
                    options=[{'label': i, 'value': i} for i in df_chalets['city'].unique()],
                    value='Coconut Grove',
                    labelStyle = {'display': 'block'}
                ),

            ], style={'fontFamily':'arial', 'fontSize':20,}), 
            width = {'size':2, 'offset':2}
        ),
        # SEGUNDA COLUMNA de la cuarta fila, esta columna contiene
        # el elemento RadioItem para seleccionar una caracterisca: 
        dbc.Col(
            html.Div([
                dcc.RadioItems(
                    id='characteristics',
                    options=[{'label': i, 'value': i} for i in df_chalets['characteristics'].unique()],
                    value='Garden',
                    labelStyle = {'display': 'block'}
                ),
               
            ], style={'fontFamily':'arial', 'fontSize':20}), 
            width = {'size':2, 'offset':4}
        )
    ], justify = 'start'),
    
    html.Hr(),  # Añade un linea horizontal
    html.Br(),

    # Se Crea la QUINTA FILA:
    dbc.Row([
        # Solo tiene una columna que va a incluir la imagen:
        dbc.Col(
            html.Div([
                html.Img(id='display-image', src='children', height=300, style = {'align' : 'center'} )
            ], style = {'text-align' : 'left'}),
        width={'offset' : 3}
        )
    ]),
])




