import sys
'''Sys= allows to stop running code at certain point. Type: sys.exit('STOP')'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt

file_path="/Users/morganharrison/Downloads/ev228_data/"
selected_name= 'Selected_Station_Observations_Daily_Xtab_202510261705.csv'
out_p= '/Users/morganharrison/Downloads/ev228_data/graphs/'
out_fn= '6_envdata_story.png'
df_csf = pd.read_csv(file_path + selected_name)
#print(df_csf.columns)

def loop_dates(df):
    df['year']= None
    df['month']= None
    for a in range(9379):
        yr = df.iloc[a, 1][2:12]
        date = pd.to_datetime(yr)
        df.iloc[a, 1] = date
        year=date.year
        month=date.month
        df.iloc[a, 8]=year
        df.iloc[a, 9]=month
    print(df)
    return df
good_dates= loop_dates(df_csf)
print(good_dates)

column_names=['Month', 'Year', 'Mean Discharge']
annual_mean=pd.DataFrame(columns=column_names)
for m in range(2000,2026):
    for l in range(1,13):
        work=good_dates.loc[(good_dates['year']==m) & (good_dates['month']==l), 'DISCHRG Value'].mean()
        print(m, l, work)
        new_row=pd.DataFrame({"Month":[l], "Year": [m], "Mean Discharge": [work]})
        annual_mean=pd.concat([annual_mean, new_row], ignore_index=True)
print(annual_mean)

data={'X_values':annual_mean['Year'],
      'Y_values':annual_mean['Mean Discharge']}
df_graph=pd.DataFrame(data)
x=df_graph['X_values']
y=df_graph['Y_values']

fig=plt.figure()
fig.patch.set_facecolor('powderblue')
ax=fig.add_subplot(1, 1, 1)
ax.set_facecolor('aliceblue')

plt.plot(x, y, linewidth=2)
plt.xlabel('Years')
plt.xlim(2000, 2025)
plt.ylabel('Stream discharge in cfs')
plt.title('South Platte River near Lake George, CO, 2000-2025')
plt.savefig(out_p + out_fn, dpi=400)
plt.show()




'''The long way, manually calculating annual DISCHRG Value, 
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