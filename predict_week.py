from pandas import read_json, read_csv
from time import time
import requests as req
from predict import get_predictor_values, predict
from tqdm import tqdm
from flask import jsonify


def predict_week():
    predictions = list()
    use_predicted = list()
    hour = (((int(time() // 86400)) * 86400 + 4 * 60 * 60) * 1000)
    feat_temp = get_predictors()
    feat_dewpt = get_predictors(dewpt=True)
    for i in tqdm(range(0, 169)):
        use_predicted.append(i)
        df_temp = get_predictor_values(hour, feat_temp, use_predicted, predictions)
        df_dewpt = get_predictor_values(hour, feat_dewpt, use_predicted, predictions)
        pred_temp = predict(df_temp)[0]
        pred_dewpt = predict(df_dewpt, dewpt=True)[0]

        predictions.append({
            'date_value': hour,
            'predicted': {
                'temp': round(pred_temp, 1),
                'dew_point': round(pred_dewpt, 1)
            }
        })
        hour += 3600000
    return {'data': predictions}
    # return predictions

# def initialize():
#     times = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00',
#              '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00',
#              '20:00', '21:00', '22:00', '23:00']
#     labels = {
#         'Temp (°C)': 'temp',
#         'Dew Point Temp (°C)': 'dew_point'
#     }


def get_predictors(dewpt=False):
    predictors = list()
    if dewpt:
        with open('training_data/dewpt_final_features.txt', 'r') as f:
            predictors = [line.strip() for line in f]
    else:
        with open('training_data/temp_final_features.txt', 'r') as f:
            predictors = [line.strip() for line in f]
    return predictors
