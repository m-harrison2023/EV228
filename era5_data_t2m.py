import pandas as pn
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

netcdf_file_path="/Users/morganharrison/Downloads/ev228_data/"
file_name= 'era5_t2m_1997-2025.nc'
ds = xr.open_dataset(netcdf_file_path + file_name)
print(ds)

temp= ds.to_array('t2m')
temp.plot()
plt.show()