#Importing needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

shp_file = "U:\Shared\GIS\StuData\ZJREEV2544\Fall_18\GISC_3200K_Python\final_project\Pandas_Map\data\tl_2010_us_state10\tl_2010_us_state10.shp"
map_frame = gpd.read_file(shp_file)
