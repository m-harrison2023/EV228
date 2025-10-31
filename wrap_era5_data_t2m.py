import era5_data_t2m.py as edt
netcdf_file_path="/Users/morganharrison/Downloads/ev228_data/"
file_name= 'era5_t2m_1997-2025.nc'

edt.fun_variable_era5(netcdf_file_path, file_name, 'longitude')

#edt.fun_descrip_era5()

#edt.fun_plot_era5(netcdf_file_path, file_name)