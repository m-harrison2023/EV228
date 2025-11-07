import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import fun_gridded
#import cartopy 

f_p="/Users/morganharrison/Downloads/ev228_data/"
f_n= 'veg_coverage_s.nc'
out_path= '/Users/morganharrison/Downloads/ev228_data/graphs/'
out_fn= '1_indvVeg.png'

da_p = fun_gridded.import_era5(file_path=f_p + f_n, var='metANN')
da_timemn= da_p.mean(dim='valid_time')
da_timemn.plot()
plt.show(da_timemn)
#fun_gridded.mapveg(da_timemn, out_path=out_path, out_name=out_fn)