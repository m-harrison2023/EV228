import pandas as pn
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

file_path="/Users/morganharrison/Downloads/ev228_data/"
file_name= 'KRDU_temp_188708-202508.csv'
df = pn.read_csv(file_path + file_name)
print(df)

df_yr= df['YEAR']
df_temp= df['metANN']

slope, intercept, r_value, p_value, std_err= stats.linregress(df_yr, df_temp)

plt.scatter(df_yr, df_temp, color='green')
plt.title('Raleigh-Durham Aiport (KRDU), Annual Mean Temp, 1887-2025')
plt.xlabel('')
plt.ylabel('')
plt.plot(df_yr, intercept + slope * df_yr)
plt.show()