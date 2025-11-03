import matplotlib.pyplot as pn
import pandas as pn
import xarray as xr
import netCDF4 as nc

#2005 Convective Precipitation and High Vegetation Cover
#fn="/Users/morganharrison/Downloads/ev228_data/"
#fp= 'data_stream-moda_stepType-avgad.nc'
#ds = nc.Dataset(fn+fp)
#print(ds)

fn="/Users/morganharrison/Downloads/ev228_data/"
fp= 'data_stream-moda_stepType-avgad.nc'
ds = xr.open_dataset(fn+fp)

plt.title('Veggetation')
plt.show()