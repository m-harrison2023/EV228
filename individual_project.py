import matplotlib.pyplot as pn
import pandas as pn
import xarray as xr
import netCDF4 as nc

fn="/Users/morganharrison/Downloads/ev228_data/"
fp= 'precip+vegetation.zip'
ds = nc.Dataset(fn+fp)
print(ds)