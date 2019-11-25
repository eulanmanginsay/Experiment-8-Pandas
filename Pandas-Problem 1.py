import pandas as pd
 pd.read_csv('cars.csv')
 cars=pd.read_csv('cars.csv')
x=cars.drop(cars.index[5:27])
x