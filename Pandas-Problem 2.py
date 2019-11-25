import pandas as pd
cars=pd.read_csv('cars.csv')
A=cars.iloc[:5,1:11:2]
B=cars[cars['Model']=='Mazda RX4']
C=cars.loc[cars['Model']=='Camaro Z28',['cyl']]
D=cars.loc[[1,28,18],['cyl','gear']]