import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import fun_gridded

f_p="/Users/morganharrison/Downloads/ev228_data/"
f_n= 'veg_coverage_s.nc'
out_path= '/Users/morganharrison/Downloads/ev228_data/graphs/'
out_fn= '9_indvVeg.png'

''' lai_hv: High veg
    lai_lv: Low veg'''
da_p = fun_gridded.import_era5(file_path=f_p + f_n, var='lai_hv')

base_period= da_p.sel(valid_time=slice("1950-01-01", "1950-12-31"))
base_mean= base_period.mean(dim='valid_time')

study_period= da_p.sel(valid_time=slice("2025-01-01", "2025-12-31"))
study_mean= study_period.mean(dim='valid_time')
change=study_mean-base_mean

#data_selected_yrs= change.sel(valid_time=slice("2020-01-01", "2020-12-31"))
fun_gridded.mapveg(change, out_path=out_path, out_name=out_fn)
