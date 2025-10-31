import era5_data_t2m as edt
netcdf_file_path="/Users/morganharrison/Downloads/ev228_data/"
file_name= 'era5_t2m_1997-2025.nc'

def_variable= edt.fun_variable_era5(netcdf_file_path, file_name, 'valid_time')
# Function to import netCDF file and selecting a variable

def_descrip= edt.fun_descrip_era5('valid_time', def_variable)
# Function to calculate descriptive statistic

edt.fun_plot_era5(def_descrip[])
# Function to make a basic map plot of data