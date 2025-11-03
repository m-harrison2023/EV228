import sys
'''Sys= allows to stop running code at certain point. Type: sys.exit('STOP')'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt

import fun_plots as fp
import fun_import as fi

file_path="/Users/morganharrison/Downloads/ev228_data/"
selected_name= 'Selected_Station_Observations_Daily_Xtab_202510261705.csv'
out_p= '/Users/morganharrison/Downloads/ev228_data/graphs/'
out_fn= '1_envdata_story.png'
df_csf = pd.read_csv(file_path + selected_name)
print(df_csf.columns)

def loop_dates(df):
    df['year']= None
    for a in range(9379):
        yr = df.iloc[a, 1][2:12]
        date = pd.to_datetime(yr)
        df.iloc[a, 1] = date
        year=date.year
        df.iloc[a, 8]=year
    print(df)
    return df
good_dates= loop_dates(df_csf)
print(good_dates)

#fp.timeseries(good_dates, in_x='''enter''', out_path=out_p, out_name=out_fn)

# dates= pd.to_datetime(df['Date Time'])
# print(dates)
# df['Year']=df['Date Time'].dt.year
# print(df['Year'])

'''The long way, manually calculating annual DISHRG Value, 
incomplete but alternative to transfer daily data into annual
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
#print(year_0, year_1, year_2, year_3, year_4, year_5, year_6, year_7, year_8, year_9, year_10, year_11, year_12, year_13)

'''