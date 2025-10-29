import pandas as pn
import numpy as np

file_path="/Users/morganharrison/Downloads/ev228_data/"
file_name= 'KRDU_temp_188708-202508.csv'
df = pn.read_csv(file_path + file_name)

#months_w= df['D-J-F']
#print(months_w, df.iloc[17])

def fun_import_code(file_path, file_name, column):
    df= pn.read_csv(file_path + file_name)
    variable_column= df[column]
    print(variable_column)

fun_import_code(file_path, file_name, 'D-J-F')