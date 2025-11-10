'''fun_plots
Taken from dmhuehol, ev228-analysis-envirnmental-data
'''
import sys

#from icecream import ic
import matplotlib.pyplot as plt

def timeseries(in_df, in_x=None, out_path='', out_name=''):
    ''' Plot timeseries from 1D dataframe '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig=plt.figure()
    fig.patch.set_facecolor("#A1BFD4")
    ax=fig.add_subplot(1, 1, 1)
    ax.set_facecolor("#C2DCE4")

    plt.plot(in_x, in_df, color="#3A094A", linewidth=2)
    plt.xlabel('years')
    plt.xlim(1948, 2025)
    plt.ylabel('annual temperature (deg C)')
    plt.title('ASM00094998, Macquarie Island, Australia, 1948-2025')
    plt.savefig(out_path + out_name, dpi=400)

def map(in_da, out_path='', out_name=''):
    ''' Plot map from 2D DataArray '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    lons = in_da.longitude
    lats = in_da.latitude

    image = plt.pcolormesh(lons, lats, in_da)
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title('ERA5 10mWind, 1980-1989')
    cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
    cb.set_label('Wind (mps)')
    plt.savefig(out_path + out_name, dpi=400)
