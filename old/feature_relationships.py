from pandas import *

df = read_csv('data/clean_training_data_year.csv', sep=',', header=0, index_col='date')
relations = df.corr()[['mean_temp']].sort_values('mean_temp')
relations.to_csv('data/relationships.csv', sep=',')
# Calculates pearson correlation coefficient between all values
print(relations)

