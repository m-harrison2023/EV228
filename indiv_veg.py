import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import fun_gridded
import cartopy.crs as ccrs
import cartopy.feature as cfeature

f_p="/Users/morganharrison/Downloads/ev228_data/"
f_n= 'veg_coverage_s.nc'
out_path= '/Users/morganharrison/Downloads/ev228_data/graphs/'
out_fn= '3_indvVeg.png'

''' lai_hv: High veg
    lai_lv: Low veg'''
da_p = fun_gridded.import_era5(file_path=f_p + f_n, var='lai_hv')
da_timemn= da_p.mean(dim='valid_time')

lons = da_timemn['longitude']
lats = da_timemn['latitude']
image = plt.pcolormesh(lons, lats, da_timemn, shading="nearest")
cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
cb.set_label('Leaf area index')
ax= plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-80, -40, -20, 10], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.RIVERS)
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.title('ERA5 Vegetation')
plt.savefig(out_path + out_fn, dpi=500)