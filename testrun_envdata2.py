import matplotlib.pyplot as plt
import geopandas as gpd

file_path="/Users/morganharrison/Downloads/ev228_data/"
historic_name= 'Historic_Fire_Perimeters.geojson'
gdf=gpd.read_file(file_path + historic_name)
print(gdf.columns)