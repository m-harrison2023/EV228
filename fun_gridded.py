'''Taken from ev228 Code from Daniel H'''
import sys
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr
import numpy as np


def mapveg(in_da, out_path='', out_name=''):
    fig = plt.figure()
    lons = in_da.longitude
    lats = in_da.latitude
    X, Y= np.meshgrid(lons, lats)
    #interval= ax.xaxis.get_view_interval()
    #ax.set_xlim(sorted(interval), auto=None)
    image = plt.pcolormesh(Y, X, in_da, shading="nearest")
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title('ERA5 Vegetation')
    cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
    cb.set_label('Leaf area index')
    plt.savefig(out_path + out_name, dpi=400)

def import_era5(file_path='', var=''):
    ''' Import ERA5 gridded data '''
    ds = xr.open_dataset(file_path)
    print(ds)
    da = ds.to_array()
    da= ds[var]
    return da