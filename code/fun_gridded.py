import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.mpl.ticker as cticker

def mapveg(in_da, out_path='', out_name=''):
    ''' Mapping figure, using cartopy and matplotlib
    Keyword arguments: 
    in_da-- assigning longitude and latitude to lons+lats 
    out_path + out_name-- saving figure and labeling in given location

    Outputs: 
    fig-- plotting figure
    '''
    fig= plt.figure()
    ax= fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    lons = in_da.longitude
    lats = in_da.latitude
    image = plt.pcolormesh(lons, lats, in_da, shading="nearest")

    '''Creating ticks, x and y axis labeling'''
    ax.set_xticks(np.arange(-80, -30, 10), crs=ccrs.PlateCarree())
    lon_formatter= cticker.LongitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.set_yticks(np.arange(-20, 20, 10), crs=ccrs.PlateCarree())
    lat_formatter= cticker.LatitudeFormatter()
    ax.yaxis.set_major_formatter(lat_formatter)

    '''Cartopy mapping, adding elements'''
    ax.coastlines()
    ax.set_extent([-80, -40, -20, 10], crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.RIVERS)

    '''Labeling and refining look'''
    fig.patch.set_facecolor("#E8FFEC")
    csfont= {'fontname':'Times New Roman'}
    cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.04)
    cb.set_label('Difference in High Leaf Area Index', **csfont)
    plt.title('Amazon Rainforest Vegetation, 1950 vs 2025', **csfont, fontweight='bold', fontsize=15)
    plt.savefig(out_path + out_name, dpi=400)

def import_era5(file_path='', var=''):
    ''' Import ERA5 gridded data '''
    ds = xr.open_dataset(file_path)
    print(ds)
    da = ds.to_array()
    da= ds[var]
    return da
