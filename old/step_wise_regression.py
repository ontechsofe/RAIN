from pandas import read_csv
from statsmodels.api import add_constant

clean_data = read_csv('data/clean_training_data.csv', sep=',', header=0, index_col='date')

predictors = ['mean_temp_1', 'max_temp_1', 'min_temp_1', 
             'mean_dewpt_1', 'max_dewpt_1', 'min_dewpt_1',
             'mean_temp_2', 'max_temp_2', 'min_temp_2', 
             'mean_dewpt_2', 'max_dewpt_2', 'min_dewpt_2',
             'mean_temp_3', 'max_temp_3', 'min_temp_3', 
             'mean_dewpt_3', 'max_dewpt_3', 'min_dewpt_3']

df = clean_data[['mean_temp'] + predictors]

x = add_constant(df[predictors]) 
y = df['mean_temp']

print(x)
x.ix[:5, :5]


