from tqdm import tqdm
from pandas import read_csv


def derive_nth_day_feature(df, feature, N):
    rows = df.shape[0]
    nth_prior_measurements = [None]*N + \
        [df[feature][i-N] for i in range(N, rows)]
    col_name = f'{feature}_{N}'
    df[col_name] = nth_prior_measurements


df = read_csv('../data/2010-2019training_data.csv', sep=',', header=0,
              index_col=['Date/Time', 'Year', 'Month', 'Day', 'Time'])
to_remove = ['Hmdx', 'Wind Chill', 'Temp Flag', 'Dew Point Temp Flag', 'Rel Hum Flag',
             'Wind Dir Flag', 'Wind Spd Flag', 'Visibility Flag', 'Stn Press Flag']
# feats = [x for x in list(df.columns) if x not in to_remove]
feats = ['Temp (°C)', 'Dew Point Temp (°C)']
df = df.sort_index(ascending=True)
df = df[feats]
# df['Weather'] = df['Weather'].fillna(value='Normal')
# days = [1, 2, 3, 4, 5, 6, 7, 365, 366, 367, 368, 369, 370, 380]

hours = [i for i in range(1, 1 + 168)] + [i for i in range(8760, 8760 + 168)] + [i for i in range(
    17520, 17520 + 168)] + [i for i in range(26280, 26280 + 168)] + [i for i in range(35040, 35040 + 168)]

for feat in tqdm(feats):
    for N in tqdm(hours):
        derive_nth_day_feature(df, feat, N)
df.dropna()
df.to_csv('training_set.csv')
