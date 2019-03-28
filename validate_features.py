from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, median_absolute_error  

df = read_csv('./training_data/clean_data_set.csv', sep=',', header=0, index_col=['Date/Time', 'Year', 'Month', 'Day', 'Time'])
X = read_csv('./training_data/final_clean_training_set.csv', sep=',', header=0, index_col=['Date/Time', 'Year', 'Month', 'Day', 'Time'])
Y = df['Temp (°C)']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)  

lr = LinearRegression()
lr.fit(X_train, Y_train)
X_test = read_csv('./training_data/march24_test.csv', sep=',', header=0, index_col=['Date/Time', 'Year', 'Month', 'Day', 'Time'])
prediction = lr.predict(X_test)
print(prediction)

print("The Explained Variance: %.2f" % lr.score(X_test, Y_test))  
print("The Mean Absolute Error: %.2f degrees celsius" % mean_absolute_error(Y_test, prediction))  
print("The Median Absolute Error: %.2f degrees celsius" % median_absolute_error(Y_test, prediction)) 