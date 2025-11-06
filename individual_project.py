import matplotlib.pyplot as pn
import pandas as pn
import numpy as np

import fun_plots as fp

'''2005 Convective Precipitation and High Vegetation Cover'''
fn="/Users/morganharrison/Downloads/ev228_data/vegetation_precip_era5/"
f_p= '2_data_stream-moda_stepType-avgad.nc'
out_fn= '/Users/morganharrison/Downloads/ev228_data/graphs/'
out_fp= '1_indvP.png'

fig_name= 'latitude'
da_veg = fi.import_era5(file_path= fn+f_p, var=fig_name)
print(da_veg)

#da_veg_time= da_veg.mean(dim='valid_time')
#fp.map(da_veg_time, out_path=out_fp, out_name=out_fn)
