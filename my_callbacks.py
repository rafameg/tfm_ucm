import base64
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output, State
from resources import data_load
from my_tabs import introduction,main_reporting, reporting_flats, reporting_chalets, gallery, main_analysis, analysis_flats, analysis_chalets
import os.path
from os import path
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
from app import app
import dash_html_components as html
import dash_table
import dash_bootstrap_components as dbc


####### Inicialización de variables importantes de dataframe 

df_flats = data_load.data_load_flats()
df_chalets = data_load.data_load_chalets()
df_flats_images = data_load.data_load_images_chalets()

#############################################################

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

@app.callback(
    Output('tabs-content-master', 'children'),
    [Input('tabs-master', 'value')])

def render_content_main(tab):
    if tab == 'Introduction':
        return introduction.tab_1_layout
    elif tab == 'Reporting':
        return main_reporting.tab_1_layout
    elif tab == "Analysis":
        return main_analysis.tab_1_layout
    elif tab == "gallery":
        return gallery.tab_1_layout
    else:
        return introduction.tab_1_layout

@app.callback(
    Output('tabs-content-reporting', 'children'),
    [Input('tabs-reporting', 'value')])

def render_content_reporting(tab):
    if tab == 'ReportingPisos':
        return reporting_flats.tab_1_layout
    elif tab == 'ReportingChalets':
        return reporting_chalets.tab_1_layout

@app.callback(
    Output('tabs-content-analysis', 'children'),
    [Input('tabs-analysis', 'value')])

def render_content_reporting(tab):
    if tab == 'AnalisisPisos':
        return analysis_flats.tab_1_layout
    elif tab == 'AnalisisChalets':
        return analysis_chalets.tab_1_layout

@app.callback(
    Output('display-image', 'src'),
    [Input('city', 'value'),
     Input('characteristics', 'value')])
def callback_image(city, characteristics):
    path = 'resources/images/'
    return encode_image(path+df_flats_images[(df_flats_images['city']==city) & (df_flats_images['characteristics']==characteristics)]['image'].values[0])

@app.callback(
    [Output("progress", "value"), Output("progress", "children")],
    [Input("progress-interval", "n_intervals")],
)
def update_progress(n):
    # check progress of some background process, in this example we'll just
    # use n_intervals constrained to be in 0-100
    progress = min(n % 110, 100)
    # only add text after 5% progress to ensure text isn't squashed too much
    return progress, f"{progress} %" if progress >= 5 else ""

### Callback input prediction flats

@app.callback(
    [Output("tabla-analisis-flats", "data"), 
     Output('tabla-analisis-flats', 'columns'),
     Output('result-prediction-flats','children')],
    [Input("input-predi_button-flats", "n_clicks")],
    [
        State("input-bed-flats", "value"),
        State("input-bath-flats", "value"),
        State("input-hbath-flats","value"),
        State("input-garage-flats", "value"),
        State("input-one_space-flats", "value"),
        State("input-living_area-flats", "value"),
        State("input-tile-flats", "value"),
        State("input-carpeted-flats", "value"),
        State("input-ceramic-flats", "value"),
        State("input-wood-flats", "value"),
        State("input-waterfront-flats", "value"),
        State("input-two_more_spaces-flats", "value"),
        State("input-ocean_view-flats", "value"),
        State("input-housing_older_person-flats", "value"),
        State("input-intercoastal_view-flats", "value"),
        State("input-pets_allowed-flats", "value"),
        State("input-style-flats", "value"),
        State("input-year_built-flats", "value"),
        State("input-us_one-flats", "value"),
        State("input-corner_unit-flats", "value"),
        State("input-zip_code-flats", "value"),
        State("input-NLOYO-flats", "value"),
        State("input-association_fee_paid-flats", "value"),
        State("input-ready_to_lease-flats", "value")
    ],
)
def generarPrediccionFlatsYGrabarDatos(n,bed,bath,hbath,garage,one_space,living_area,tile,carpeted,ceramic,wood,waterfront,two_more_spaces,ocean_view,housing_older,intercoastal,pets,style,year_built,us_one,corner_unit,zip_code,nloyo,association_fee,ready_to_lease):
    if n is None:
        raise PreventUpdate
    else:
        lista = []
        lista2 = []
        print("Showing input data flats prediction: ")
        print("bed: " + str(bed))
        print("bath: " + str(bath))
        print("hbath: " + str(hbath))
        print("garage: " + str(garage))
        print("one_space: " + str(one_space))
        print("living_area: " + str(living_area))
        print("tile: " + str(tile))
        print("carpeted: " + str(carpeted))
        print("ceramic: " + str(ceramic))
        print("wood: " + str(wood))
        print("waterfront: " + str(waterfront))
        print("two_more_spaces: " + str(two_more_spaces))
        print("ocean_view: " + str(ocean_view))
        print("housing_older: " + str(housing_older))
        print("intercoastal: " + str(intercoastal))
        print("pets: " + str(pets))
        print("style: " + str(style))
        print("year_built: " + str(year_built))
        print("us_one: " + str(us_one))
        print("corner_unit: " + str(corner_unit))
        print("zip_code: " + str(zip_code))
        print("nloyo: " + str(nloyo))
        print("association_fee: " + str(association_fee))
        print("ready_to_lease: " + str(ready_to_lease))

        #### Construimos nuestro data frame
        lista.extend((bath,style,hbath,living_area,year_built,association_fee,carpeted,ocean_view,one_space,pets,waterfront,intercoastal,nloyo,garage,ceramic,tile,bed,housing_older,two_more_spaces,wood,us_one,ready_to_lease,corner_unit,zip_code))
        lista2.append(lista)
        columnas = ['FBaths', 'Style', 'HBaths', 'SqFt_Liv_Area', 'Year_Built', 'Assoc_Fee_Paid', 'Carpeted', 'Ocean_View', 'One_Space', 'Pets_Allowed', 'Waterfront', 'Intracoastal_View', 'No_Lease_Onest_Year_Owned', 'Garage_Spaces', 'Ceramic', 'Tile', 'Beds', 'Housing_Older_Persons_Act', 'Two_Or_More_Spaces', 'Wood', 'East_Of_Us_One', 'Ok_To_Lease', 'Corner_Unit', 'Zip_Code']
        df_final = pd.DataFrame(lista2,columns=columnas)
        #######

        # Obtenemos resultado binario del modelo

        resultado_modelo_binario_prediccion = data_load.model_flats_XGBM_Binary_predict(df_final)
        resultado_modelo_binario = resultado_modelo_binario_prediccion[0]
        print("Resultado modelo binario: " + str(resultado_modelo_binario))

        prediccion_precio = None
        ###### Comprobamos el resultado del modelo, si el resultado es 0 se aplica el modelo de menores de 600000, en caso contrario, el de mayores

        if resultado_modelo_binario == 0:
            prediccion_precio = data_load.model_flats_XGBM_lower_predict(df_final)
        else:
            prediccion_precio = data_load.model_flats_XGBM_bigger_predict(df_final)

        print("El precio que arroja el modelo es: " + str(prediccion_precio[0]))
        
        df_final['Predicted_Price'] = prediccion_precio[0]
        data, columns = None, None
        if path.exists('resources/models_results_data/flats_results.csv'):
            current_df = pd.read_csv('resources/models_results_data/flats_results.csv')
            current_df = current_df.append(df_final,ignore_index=True)
            current_df.to_csv('resources/models_results_data/flats_results.csv', index=False)
            data = current_df.to_dict('rows')
            columns = [{"name": i, "id": i,} for i in (current_df.columns)]
        else:
            df_final.to_csv('resources/models_results_data/flats_results.csv',index=False)
            data = df_final.to_dict('rows')
            columns = [{"name": i, "id": i,} for i in (df_final.columns)]

        return data,columns,f'The predicted price for this property is ${prediccion_precio[0]}'



### Callbacks para la ventana de reporting de flats #######

@app.callback(
    Output('intermediate_filter_data_flats', 'data'),
    [Input('filter-city-flats', 'value'),
     Input('filter-price-flats','value')]
)


# El segundo paso es crear el METODO para almacenar los valores comentados.
# Este metodo basicamente incluye una QUERY que filtra dos datos segun lo que
# se incluya en el INPUT y manda esos datos al STORE en formato JSON:
def save_filter_data(cities,prices):
    # En primer lugar se crea una copia del dataframe original:
    df_filter = df_flats.copy()
    # Se realiza el filtrado de los datos:
    # Un primer condicional IF para ciudades:
    if len(cities) > 0:
        df_filter = df_filter.query(f'City_Name in ({cities})')
    # Un segundo condicional IF para precios:
    if prices is not None:
        if prices == "":
            df_filter = df_filter.query(f'Sale_Price <= 9999999999999999')
        else:  
            df_filter = df_filter.query(f'Sale_Price <= {prices}')  
    
    # Por ultimo, se devuelve el formato JSON:
    
    return df_filter.to_json()

# Y el tercer paso es crear otro CALLBACK para hacer que la tabla lea
# los datos almacenados en el STORE:
@app.callback(
    
    [Output('table-flats', 'data'),
     Output('map-flats','figure'),
     Output('indicator-ownerships-flats','value'),
     Output('indicator-min-price-flats','value'),
     Output('indicator-max-price-flats','value')],
    [Input('intermediate_filter_data_flats', 'data')] 
)

# Y creamos el metodo correspondiente:
def update_data(data_json): # Lo que recibe esta funcion son los datos en formato JSON,
                            # que corresponden a los datos ya filtrados segun los dropdown
    # Lo primero es leer esos datos recibidos:
    df_filter_graph = pd.read_json(data_json)
    # Se devuelven los valores, hay que tener en cuenta que se
    # devuelve un diccionario de registros:
    return [
                df_filter_graph.to_dict('records'),
                {
                    'data': get_data_map(df_filter_graph),
                    'layout': dict(
                        autosize = True,
                        hovermode = 'closest',
                        showlegend = False,
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

                },
                df_filter_graph.shape[0],
                df_filter_graph['Sale_Price'].min(),
                df_filter_graph['Sale_Price'].max()
            ]


def get_data_map(df_filter_graph):
    
    markers = [
        go.Scattermapbox(
            lat=df_filter_graph.latitude,
            lon=df_filter_graph.longitude,
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=10
            ),
            text=df_filter_graph.City_Name,
            name = 'City',
            legendgroup="City",
        )
       
    ]
    return markers


##################################################################################################


### Callbacks para la ventana de reporting de Chalets #######

@app.callback(
    Output('intermediate_filter_data_chalets', 'data'),
    [Input('filter-city-chalets', 'value'),
     Input('filter-price-chalets','value')]
)


# El segundo paso es crear el METODO para almacenar los valores comentados.
# Este metodo basicamente incluye una QUERY que filtra dos datos segun lo que
# se incluya en el INPUT y manda esos datos al STORE en formato JSON:
def save_filter_data(cities,prices):
    # En primer lugar se crea una copia del dataframe original:
    df_filter = df_chalets.copy()
    # Se realiza el filtrado de los datos:
    # Un primer condicional IF para ciudades:
    if len(cities) > 0:
        df_filter = df_filter.query(f'City_Name in ({cities})')
    # Un segundo condicional IF para precios:
    if prices is not None:
        if prices == "":
            df_filter = df_filter.query(f'Sale_Price <= 9999999999999999')
        else:  
            df_filter = df_filter.query(f'Sale_Price <= {prices}')  
    
    # Por ultimo, se devuelve el formato JSON:
    
    return df_filter.to_json()

# Y el tercer paso es crear otro CALLBACK para hacer que la tabla lea
# los datos almacenados en el STORE:
@app.callback(
    
    [Output('table-chalets', 'data'),
     Output('map-chalets','figure'),
     Output('indicator-ownerships-chalets','value'),
     Output('indicator-min-price-chalets','value'),
     Output('indicator-max-price-chalets','value')],
    [Input('intermediate_filter_data_chalets', 'data')] 
)

# Y creamos el metodo correspondiente:
def update_data(data_json): # Lo que recibe esta funcion son los datos en formato JSON,
                            # que corresponden a los datos ya filtrados segun los dropdown
    # Lo primero es leer esos datos recibidos:
    df_filter_graph = pd.read_json(data_json)
    # Se devuelven los valores, hay que tener en cuenta que se
    # devuelve un diccionario de registros:
    return [
                df_filter_graph.to_dict('records'),
                {
                    'data': get_data_map(df_filter_graph),
                    'layout': dict(
                        autosize = True,
                        hovermode = 'closest',
                        showlegend = False,
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

                },
                df_filter_graph.shape[0],
                df_filter_graph['Sale_Price'].min(),
                df_filter_graph['Sale_Price'].max()
            ]


def get_data_map(df_filter_graph):
    markers = [
        go.Scattermapbox(
            lat=df_filter_graph.latitude,
            lon=df_filter_graph.longitude,
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=10
            ),
            text=df_filter_graph.City_Name,
            name = 'City',
            legendgroup="City",
        )
       
    ]
    return markers

#####################################################################################

### Validación Email Flats


@app.callback(
    [Output(component_id='output-userEmail-flats', component_property='children'),
     Output(component_id='output-userEmailStatus-flats', component_property='value')],
    [Input(component_id='input-userEmail-flats', component_property='value')]
)
def update_output_div(input_value):
    emails_df = data_load.data_load_users_validated()
    if input_value in emails_df.values:
        return ["Validated",1]
    return ["Non validated",0]
    
#####################################################################################

### Validación Email Chalets


@app.callback(
    [Output(component_id='output-userEmail-chalets', component_property='children'),
     Output(component_id='output-userEmailStatus-chalets', component_property='value')],
    [Input(component_id='input-userEmail-chalets', component_property='value')]
)
def update_output_div(input_value):
    emails_df = data_load.data_load_users_validated()
    if input_value in emails_df.values:
        return ["Validated",1]
    return ["Non validated",0]

#####################################################################################

####### Callbacks Chalets Predictions ##########
@app.callback(
    [Output("tabla-analisis-chalets", "data"), 
     Output('tabla-analisis-chalets', 'columns'),
     Output('result-prediction-chalets','children'),
     Output('output-data-recomenacion','children')],
    [Input('input-predi_button-chalets', 'n_clicks')],
    [State('input-bed-chalets', 'value'), 
      State('input-bath-chalets', 'value'), 
      State('input-hoa-chalets', 'value'), 
      State('input-pool-chalets', 'value'), 
      State('input-garage-chalets', 'value'), 
      State('input-built_year-chalets', 'value'), 
      State('input-waterfront-chalets', 'value'), 
      State('input-living_area-chalets', 'value'),
      State('input-zip-code-chalets', 'value'),
      State('input-dom-chalets', 'value')]
)
def update_result_chalets(n, bed, bath, hoa, pool, garage, built_year, waterfront, living_area, zip_code, dom):
    if n is None:
        raise PreventUpdate
    else :
        print("Input Bed: " + str(bed))
        print("Input bath: " + str(bath))
        print("Input hoa: " + str(hoa))
        print("Input pool: " + str(pool))
        print("Input garage: " + str(garage))
        print("Input built year: " + str(built_year))
        print("Input waterfront: " + str(waterfront))
        print("Input living area: " + str(living_area))
        print("Input zip code: " + str(zip_code))
        print("Input dom: " + str(dom))
        

        #### Construimos nuestro data frame para el modelo binario
        listaBinario = []
        listaBinario2 = []
        listaBinario.extend((living_area,zip_code,bath,built_year,pool,hoa,waterfront))
        listaBinario2.append(listaBinario)
        columnasBinario = ['est_sqft_liv_area','est_valor_zipcode','est_num_baths','est_year_built','pool_yn.Yes','association_fee.yes', 'waterfront_property_yn.Yes']
        df_Binario = pd.DataFrame(listaBinario2,columns=columnasBinario)
        
        #######
        # Obtenemos resultado binario del modelo
        
        resultado_modelo_binario_prediccion = data_load.model_chalets_XGBM_Binary_predict(df_Binario)
        resultado_modelo_binario = resultado_modelo_binario_prediccion[0]
        print("Resultado modelo binario: " + str(resultado_modelo_binario))

        prediccion_precio = None
        df_modeloFinal = None

        if resultado_modelo_binario == 0:
            columnasModelo = ['est_sqft_liv_area','est_valor_zipcode', 'est_num_beds', 'est_num_baths','est_year_built','pool_yn.Yes','est_garage_spaces']
            listaModeloFinal = []
            listaModeloFinal2 = []
            listaModeloFinal.extend((living_area,zip_code,bed,bath,built_year,pool,garage))
            listaModeloFinal2.append(listaModeloFinal)
            df_modeloFinal = pd.DataFrame(listaModeloFinal2,columns=columnasModelo)
            prediccion_precio = data_load.model_chalets_XGBM_lower_predict(df_modeloFinal)
        else:
            columnasModelo = ['est_sqft_liv_area','est_valor_zipcode','est_num_beds','est_num_baths', 'est_year_built', 'waterfront_property_yn.Yes', 'est_dom']
            listaModeloFinal = []
            listaModeloFinal2 = []
            listaModeloFinal.extend((living_area,zip_code,bed,bath,built_year,waterfront,dom))
            listaModeloFinal2.append(listaModeloFinal)
            df_modeloFinal = pd.DataFrame(listaModeloFinal2,columns=columnasModelo)
            prediccion_precio = data_load.model_chalets_XGBM_bigger_predict(df_modeloFinal)

        df_modeloFinal['Predicted_Price'] = prediccion_precio[0]
        data,columns = None,None
        if path.exists('resources/models_results_data/chalets_results.csv'):
            current_df = pd.read_csv('resources/models_results_data/chalets_results.csv')
            current_df = current_df.append(df_modeloFinal,ignore_index=True)
            current_df.to_csv('resources/models_results_data/chalets_results.csv', index=False)
            data = current_df.to_dict('rows')
            columns = [{"name": i, "id": i,} for i in (current_df.columns)]
        else:
            df_modeloFinal.to_csv('resources/models_results_data/chalets_results.csv',index=False)
            data = df_modeloFinal.to_dict('rows')
            columns = [{"name": i, "id": i,} for i in (df_modeloFinal.columns)]


        recomendacion = data_load.recomendador_obtener_recomendacion(bed,bath,garage,hoa,pool,waterfront,living_area,built_year,zip_code,dom,prediccion_precio[0])
        print(recomendacion)
        if recomendacion.empty == False:
            figura = html.Div([
                            html.Hr(),
                            dbc.Row([html.P("Se han encontrado datos de inmuebles similares a los que estás interesado en vender. ")]),
                            dbc.Row([
                                dbc.Col( 
                                    dash_table.DataTable(
                                                        data = recomendacion.to_dict('records'),
                                                        columns=[{'name': i, 'id': i} for i in recomendacion.columns]
                                                        )
                                )
                            ])

                        ])
        else:
            figura = html.Div([
                                html.Hr(),
                                html.P("No se ha encontrado ninguna recomendación. ")
                            ])

        #dataRecomendador = recomendacion.to_dict('rows')
        #columnsRecomendador = [{"name": i, "id": i,} for i in (dataRecomendador.columns)]



        return data,columns,f'The predicted price for this property is ${prediccion_precio[0]}', figura

