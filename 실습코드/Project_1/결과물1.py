import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('SeoulBikeData_new.csv')
df = df[['Snowfall','Rented Bike Count']]
df = df[df['Snowfall'] != 0.0]
df.dropna(inplace=True)
df = df.sort_values(by='Snowfall')
print(df)
Q1 = df['Rented Bike Count'].quantile(0.25)
Q3 = df['Rented Bike Count'].quantile(0.75) 
IQR = Q3 - Q1
lowerbound = Q1 - 1.5 * IQR
upperbound = Q3 + 1.5 * IQR
dfclear = df[(df['Rented Bike Count'] >= lowerbound) & (df['Rented Bike Count'] <= upperbound)]
dfclear.corr()
plt.scatter(dfclear['Snowfall'],dfclear['Rented Bike Count'])
plt.show()