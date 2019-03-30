from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, median_absolute_error 
from joblib import dump 

df = read_csv('./training_data/clean_data_set.csv', sep=',', header=0, index_col=['Date/Time', 'Year', 'Month', 'Day', 'Time'])
X = read_csv('./training_data/final_clean_training_set_temp.csv', sep=',', header=0, index_col=['Date/Time', 'Year', 'Month', 'Day', 'Time'])
Y = df['Temp (°C)']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)  

model = LinearRegression()
model.fit(X_train, Y_train)
# X_test = read_csv('./training_data/march24_test_dewpt.csv', sep=',', header=0, index_col=['Date/Time', 'Year', 'Month', 'Day', 'Time'])
prediction = model.predict(X_test)
# print(prediction)
dump(model, './models/scikit/temp_model.joblib')

print(f'The Explained Variance: {model.score(X_test, Y_test)}')  
print(f'The Mean Absolute Error: {mean_absolute_error(Y_test, prediction)} degrees celsius')  
print(f'The Median Absolute Error: {median_absolute_error(Y_test, prediction)} degrees celsius')