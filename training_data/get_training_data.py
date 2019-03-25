import os
from pandas import read_csv, DataFrame, concat

def concat_data(directory):
    data_frames = list()
    i = 0
    for file_name in os.listdir(directory):
        data_frames.append(read_csv(f'{directory}{file_name}', sep=',', header=13))
    df = concat(data_frames, sort=False).dropna(axis='columns', how='all')
    df.set_index(['Date/Time', 'Year', 'Month', 'Day', 'Time'], inplace=True)
    return df.dropna(how='all').sort_index()


df = concat_data('../data/env_canada/')
# print(df)
df.to_csv('../data/2010-2019training_data.csv', sep=',')