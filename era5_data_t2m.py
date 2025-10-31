import pandas as pn
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

netcdf_file_path="/Users/morganharrison/Downloads/ev228_data/"
file_name= 'era5_t2m_1997-2025.nc'
ds = xr.open_dataset(netcdf_file_path + file_name)

temp= ds.to_array('t2m')
temp.plot()
#plt.title('Temp 2M')
#plt.show()

def fun_variable_era5(netcdf_file_path, file_name, column):
    ds= xr.open_dataset(netcdf_file_path + file_name)
    variable_column= ds[column]
    print(variable_column)
    return variable_column


def fun_descrip_era5(variable_column, da):
    dict_s= {
        "Mean": da.mean(variable_column),
        "Min": da.min(variable_column),
        "Max": da.max(variable_column),
        #"STD": da.std(variable_column)
}
    return dict_s


def fun_plot_era5(dict_s): 
    dict_s.plot()
    plt.title('T2M')
    plt.show()
