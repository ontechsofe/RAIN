from pandas import *


df = read_csv('data/clean_training_data.csv', sep=',', header=0, index_col='date')

# Calculates pearson correlation coefficient between all values
print(df.corr()[['mean_temp']].sort_values('mean_temp'))

# plt = df.plot.scatter("mean_temp", "mean_temp_2")