from pandas import read_json, read_csv
from time import time
import requests as req
from predict import get_predictor_values, predict
from tqdm import tqdm


def predict_week():
    predictions = list()
    use_predicted = list()
    hour = (((int(time() // 86400)) * 86400 + 4 * 60 * 60) * 1000)
    feat_temp = get_predictors()
    feat_dewpt = get_predictors(dewpt=True)
    for i in tqdm(range(0, 1)):
        use_predicted.append(i)
        df_temp = get_predictor_values(hour, feat_temp, use_predicted, predictions)
        df_dewpt = get_predictor_values(hour, feat_dewpt, use_predicted, predictions)
        pred_temp = predict(df_temp)[0]
        pred_dewpt = predict(df_dewpt, dewpt=True)[0]

        predictions.append({
            'date_value': hour,
            'data': {
                'temp': round(pred_temp, 2),
                'dewpt': round(pred_dewpt, 2)
            }
        })
        hour += 3600000

    return predictions

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
        df = read_csv('training_data/final_clean_training_set_dewpt.csv',
                      index_col=['Date/Time', 'Year', 'Month', 'Day', 'Time'])
        predictors = df.columns
    else:
        df = read_csv('training_data/final_clean_training_set_temp.csv',
                      index_col=['Date/Time', 'Year', 'Month', 'Day', 'Time'])
        predictors = df.columns
    predictors = [p.replace('Dew Point Temp (°C)', 'dew_point')
                  for p in predictors]
    predictors = [p.replace('Temp (°C)', 'temp') for p in predictors]

    return predictors
