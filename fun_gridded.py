'''Taken from ev228 Code from Daniel H'''
import sys
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr


def mapveg(in_da, out_path='', out_name=''):
    ''' Plot map from 2D DataArray '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    lons = in_da.longitude
    lats = in_da.latitude
    image = plt.pcolormesh(lons, lats, in_da)
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title('ERA5 Vegetation')
    cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
    cb.set_label('Unit')
    plt.savefig(out_path + out_name, dpi=400)

def import_era5(file_path='', var=''):
    ''' Import ERA5 gridded data '''
    ds = xr.open_dataset(file_path)
    print(ds)
    da = ds.to_array()

    return da