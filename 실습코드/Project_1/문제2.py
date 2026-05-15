import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix

df = pd.read_csv('SeoulBikeData_new.csv')

# 이상치 제거

temp_df = df[df['Rented Bike Count'] < 20000]


Q1 = temp_df['Rented Bike Count'].quantile(0.25)
Q3 = temp_df['Rented Bike Count'].quantile(0.75)
IQR = Q3 - Q1


lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR


df_clean = df[(df['Rented Bike Count'] >= lower_bound) & (df['Rented Bike Count'] <= upper_bound)].copy()

print(df_clean)
#pd.plotting.scatter_matrix 
cols = ['Temperature', 'Humidity', 'Rented Bike Count']
scatter_matrix(df[cols], alpha=0.5, figsize=(12, 12), diagonal='kde', color='blue')
plt.suptitle('Temp  Humidity  Bike Count Correlation Matrix', fontsize=15)
plt.show()

bins = list(range(-20, 41, 5))
df_clean['Temp_Bin'] = pd.cut(df_clean['Temperature'], bins=bins)

# 구간별 평균 대여량 계산
temp_res = df_clean.groupby('Temp_Bin', observed=True)['Rented Bike Count'].mean().reset_index()

# 막대그래프
plt.figure(figsize=(12, 6))
sns.barplot(data=temp_res, x='Temp_Bin', y='Rented Bike Count', palette='YlOrRd')
plt.title('Average Bike Demand by Temperature Range (5°C)', fontsize=15)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()






