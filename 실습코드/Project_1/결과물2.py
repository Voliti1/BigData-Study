import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('SeoulBikeData_new.csv')
df = df[['Snowfall','Rented Bike Count']]
df = df[df['Snowfall'] != 0.0]
df = df[df['Rented Bike Count'] < 20000]
df_clean = df.dropna()
df_clean.corr()
df_clean.plot.scatter(x='Snowfall', y='Rented Bike Count')
plt.ylim(0, 1600)
plt.show()