'''Taken from ev228 Code from Daniel H'''
import sys
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def mapveg(in_da, out_path='', out_name=''):
    fig= plt.figure()
    ax= fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    lons = in_da.longitude
    lats = in_da.latitude
    image = plt.pcolormesh(lons, lats, in_da, shading="nearest")
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title('ERA5 Vegetation')
    cb = plt.colorbar(image, shrink=.75, orientation="horizontal", pad=.02)
    cb.set_label('South America, High Leaf Coverage')
    ax.set_extent([-80, -40, -20, 10], crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.RIVERS)
    plt.savefig(out_path + out_name, dpi=400)

def import_era5(file_path='', var=''):
    ''' Import ERA5 gridded data '''
    ds = xr.open_dataset(file_path)
    print(ds)
    da = ds.to_array()
    da= ds[var]
    return da