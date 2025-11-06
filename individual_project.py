import matplotlib.pyplot as pn
import numpy as np
import xarray as xr

import fun_gridded as fg

'''2005 Convective Precipitation and High Vegetation Cover'''
f_p="/Users/morganharrison/Downloads/ev228_data/vegetation_precip_era5/"
f_n= '2_data_stream-moda_stepType-avgad.nc'
out_path= '/Users/morganharrison/Downloads/ev228_data/graphs/'
out_fn= '1_indvP.png'

variable= 'tp'
da = fg.import_era5(file_path=f_p + f_n, var=variable)
da_timemn= da.mean(dim='valid_time')
fg.map(da_timemn, out_path=out_path, out_name=out_fn)
