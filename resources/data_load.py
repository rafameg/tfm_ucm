import pandas as pd
import xgboost as xgb
import joblib



def data_load_flats():
	df = pd.read_csv('resources/flats_final_reporting_data.csv', sep = ';')
	return df

def data_load_chalets():
	df = pd.read_csv('resources/chalets_final_reporting_data.csv', sep = ';')
	return df

def data_load_images_chalets():
	df = pd.read_csv('resources/chalets.csv', sep=',')
	return df

def data_load_input_data():
	df = pd.read_csv('resources/output_data.csv',sep=',')
	return df

def data_load_users_validated():
	df = pd.read_csv('resources/users_validated_data.csv',sep=',')
	return df

def model_flats_XGBM_Binary_predict(input_data):
	model = joblib.load('resources/models/model_XGBM_Flats_Binary.model')
	return model.predict(input_data)

def model_flats_XGBM_bigger_predict(input_data):
	model = joblib.load('resources/models/model_XBGM_Flats_Bigger.model')
	return model.predict(xgb.DMatrix(input_data))

def model_flats_XGBM_lower_predict(input_data):
	model = joblib.load('resources/models/model_XGBM_Flats_Lower.model')
	return model.predict(xgb.DMatrix(input_data))

def model_chalets_XGBM_Binary_predict(input_data):
	model = joblib.load('resources/models/model_XGBM_Chalets_Binary.model')
	return model.predict(input_data)

def model_chalets_XGBM_bigger_predict(input_data):
	model = joblib.load('resources/models/model_XBGM_Chalets_Bigger.model')
	return model.predict(input_data)

def model_chalets_XGBM_lower_predict(input_data):
	model = joblib.load('resources/models/model_XGBM_Chalets_Lower.model')
	return model.predict(input_data)