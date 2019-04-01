from pandas import read_csv

df = read_csv('clean_data_set.csv', sep=',', header=0, index_col=['Date/Time', 'Year', 'Month', 'Day', 'Time'])
relations = df.corr()[['Temp (°C)']].sort_values('Temp (°C)').T
print(relations)
relevant = [f'{c}\n' for c in relations.columns if relations[c][0] >= 0.6]

relevant.remove('Dew Point Temp (°C)\n')
relevant.remove('Temp (°C)\n')

print(relevant)
with open('temp_relevant_features_2.txt', 'w') as out_file:
    out_file.writelines(relevant)