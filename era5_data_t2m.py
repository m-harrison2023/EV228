import pandas as pn
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

netcdf_file_path="/Users/morganharrison/Downloads/ev228_data/"
file_name= 'era5_t2m_1997-2025.nc'
ds = xr.open_dataset(netcdf_file_path + file_name)
da=ds['t2m']

#temp= ds.to_array('t2m')
#temp.plot()
#plt.title('Temp 2M')
#plt.show()

def fun_variable_era5(netcdf_file_path, file_name, column):
    ds= xr.open_dataset(netcdf_file_path + file_name)
    variable_column= ds[column]
    print(variable_column)
    return variable_column


def fun_descrip_era5(variable_column):
    dict_s= {
        1: da.mean[variable_column],
        2: da.min[variable_column],
        3: da.max[variable_column],
        4: da.stdev[variable_column]
}
    return dict_s


def fun_plot_era5(netcdf_file_path, file_name):
    ds= xr.open_dataset(netcdf_file_path + file_name)
    da_t2m= ds['t2m']
    da_t2m_timestat=da_t2m.sum('valid_time')
    da_t2m_index=da_t2m.isel('valid_time')
    da_t2m_index.plot()
    plt.title('T2M')
    plt.show()
    return 
