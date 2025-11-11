import matplotlib.pyplot as py
import numpy as nm
import xarray as xr

import fun_plots as fp
import fun_import as fi

#Gridded Data for ERA5 Wind
f_p="/Users/morganharrison/Downloads/ev228_data/"
f_n= 'era5_10mwind_1980-1989.nc'
out_path= '/Users/morganharrison/Downloads/ev228_data/graphs'
out_fn= '3_Era5_wind'

da = fi.import_era5(file_path=f_p + f_n, var='si10')
da_timemn = da.mean(dim='valid_time')
fp.map(da_timemn, out_path=out_path, out_name=out_fn)
