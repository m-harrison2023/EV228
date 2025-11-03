import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt

file_path="/Users/morganharrison/Downloads/ev228_data/"
selected_name= 'Selected_Station_Observations_Daily_Xtab_202510261705.csv'
df = pd.read_csv(file_path + selected_name)
print(df.columns)
#df.plot()
#plt.title('Discharge Value')
#plt.show()

def envdata_code(file_path, selected_name, column):
    df= pd.read_csv(file_path + selected_name)
    variable_column= df[column]
    print(variable_column)
    df['Year']=df['Date'].dt.year
    print(type(df.loc['Date']))
    return variable_column

#envdata_code(file_path, selected_name, 'DISCHRG Value')

year_0= df.iloc[:364]['DISCHRG Value'].mean()
year_1= df.iloc[365:729]['DISCHRG Value'].mean()
year_2= df.iloc[729:1093]['DISCHRG Value'].mean()
year_3= df.iloc[1093:1457]['DISCHRG Value'].mean()
year_4= df.iloc[1457:1821]['DISCHRG Value'].mean()
year_5= df.iloc[1821:2185]['DISCHRG Value'].mean()
year_6= df.iloc[2185:2550]['DISCHRG Value'].mean()
year_7= df.iloc[2500:2915]['DISCHRG Value'].mean()
year_8= df.iloc[2915:3280]['DISCHRG Value'].mean()
year_9= df.iloc[3280:3650]['DISCHRG Value'].mean()
year_10= df.iloc[3650: 4010]['DISCHRG Value'].mean()
year_11= df.iloc[2915: 3280]['DISCHRG Value'].mean()
year_12= df.iloc[3280:4375]['DISCHRG Value'].mean()
year_13=df.iloc[4375:4740]['DISCHRG Value'].mean()
print(year_0, year_1, year_2, year_3, year_4, year_5, year_6, year_7, year_8, year_9, year_10, year_11, year_12, year_13)

.plot()
plt.title('Discharge Value')
plt.show()