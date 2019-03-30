from pandas import read_csv

df = read_csv('clean_data_set.csv', sep=',', header=0, index_col=['Date/Time', 'Year', 'Month', 'Day', 'Time'])
relations = df.corr()[['Temp (°C)']].sort_values('Temp (°C)').T
relevant = [f'{c}\n' for c in relations.columns if relations[c][0] >= 0.8]

relevant.remove('Dew Point Temp (°C)\n')
relevant.remove('Temp (°C)\n')

with open('temp_relevant_features.txt', 'w') as out_file:
    out_file.writelines(relevant)