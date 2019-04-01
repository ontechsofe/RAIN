from pandas import read_csv

df = read_csv('training_data/final_clean_training_set_temp_2.csv', index_col=['Date/Time', 'Year', 'Month', 'Day', 'Time'])
predictors = df.columns
predictors = [x.replace('Dew Point Temp (°C)', 'dew_point') for x in predictors]
predictors = [x.replace('Temp (°C)', 'temp') for x in predictors]

with open('training_data/temp_final_features_2.txt', 'w') as f:
    predictors = [f'{x}\n' for x in predictors]
    f.writelines(predictors)