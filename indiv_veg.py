import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import fun_gridded

f_p="/Users/morganharrison/Downloads/ev228_data/"
f_n= 'veg_coverage_s.nc'
out_path= '/Users/morganharrison/Downloads/ev228_data/graphs/'
out_fn= '6_indvVeg.png'

''' lai_hv: High veg
    lai_lv: Low veg'''
da_p = fun_gridded.import_era5(file_path=f_p + f_n, var='lai_hv')
#print(da_p)
selected_date= '2025-01-01'
data_selected_yrs= da_p.sel(valid_time=selected_date)
#da_timemn= data_selected_yrs.mean(dim='valid_time')
fun_gridded.mapveg(data_selected_yrs, out_path=out_path, out_name=out_fn)