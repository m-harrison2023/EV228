import matplotlib.pyplot as py
import numpy as np
import pandas as pn

import fun_plots as fp
import fun_import as fi

#Timeseries of ASM00094998
f_p="/Users/morganharrison/Downloads/ev228_data/"
f_n= 'ASM00094998_temp_194804-202508.csv'
out_path= '/Users/morganharrison/Downloads/ev228_data/graphs/'
out_fn= '3_ASM.png'

df_data, df_yr = fi.import_ghcn(file_path=f_p + f_n, var='metANN')
filter_data = df_data[df_data != 999.9]
filter_year = df_yr[df_data != 999.9]

print(df_data)
fp.timeseries(filter_data, in_x=filter_year, out_path=out_path, out_name=out_fn)

mean_var = np.mean(filter_data)
stdev_var = np.std(filter_data)
max_var = np.max(filter_data)
min_var = np.min(filter_data)
print(mean_var, stdev_var, max_var, min_var)
