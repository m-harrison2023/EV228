import matplotlib.pyplot as pn
import numpy as np
import xarray as xr
import fun_gridded
#import cartopy 

'''2005 Convective Precipitation and High Vegetation Cover'''
f_p="/Users/morganharrison/Downloads/ev228_data/vegetation_precip_era5/"
f_n_precip= '2_data_stream-moda_stepType-avgad.nc'
f_n_veg= 'data_stream-moda_stepType-avgua.nc'
out_path= '/Users/morganharrison/Downloads/ev228_data/graphs/'
out_fn_p= '2_indvP.png'
out_fn_v= '1_indvVeg.png'

''' tp= total precipitation'''
da_p = fun_gridded.import_era5(file_path=f_p + f_n_precip, var='tp')
da_timemn= da_p.mean(dim='valid_time')
fun_gridded.mapveg(da_timemn, out_path=out_path, out_name=out_fn_p)

''' cvh= high veg
    cvl= low veg
    tvh= '''
da_v = fun_gridded.import_era5(file_path=f_p + f_n_veg, var='cvh')
da_timemn= da_p.mean(dim='valid_time')
fun_gridded.map(da_timemn, out_path=out_path, out_name=out_fn_v)
