import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt

file_path="/Users/morganharrison/Downloads/ev228_data/"
selected_name= 'Selected_Station_Observations_Daily_Xtab_202510261705.csv'
df = pd.read_csv(file_path + selected_name)
#print(df.columns)

def envdata_code(file_path, selected_name, column):
    df= pd.read_csv(file_path + selected_name)
    variable_column= df[column]
    print(variable_column)
    #df['Date']=df['Date'].year
    print(type(df.loc['Date']))

envdata_code(file_path, selected_name, 'DISCHRG Value')


#df.plot()
#plt.title('Discharge')
#plt.show()