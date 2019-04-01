from joblib import load
import requests as req
from pandas import DataFrame
from tqdm import tqdm


def predict(df, dewpt=False) -> list:
    model = None
    if dewpt:
        model = load('models/dewpt_model.joblib')
    else:
        model = load('models/temp_model.joblib')
    # df = read_csv('training_data/march24_test_temp.csv', index_col=['Date/Time', 'Year', 'Month', 'Day', 'Time'])
    return model.predict(df)


def get_predictor_values(epoch_time, predictors, use_predicted, predictions):
    values = dict()
    values['date_value'] = epoch_time
    for p in tqdm(predictors):
        val = 0.0
        if 'temp' in p:
            digits = int(p.split('_')[1])
            resp = req.get(
                f'http://sofe3720.ml/ec/past/{epoch_time}/{digits}').json()['message']['data']
            if digits in use_predicted and len(resp) > 0:
                val = predictions[len(predictions)-digits]['predicted']['temp']
            elif len(resp) > 0:
                val = resp[0]['temp']
        else:
            digits = int(p.split('_')[2])
            resp = req.get(
                f'http://sofe3720.ml/ec/past/{epoch_time}/{digits}').json()['message']['data']
            if digits in use_predicted and len(resp) > 0:
                val = predictions[len(predictions)-digits]['predicted']['dew_point']
            elif len(resp) > 0:
                val = resp[0]['dew_point']
        values[p] = val
    df = DataFrame.from_dict(values, orient='index')
    df = df.T.set_index('date_value')
    # print(df)
    return df
