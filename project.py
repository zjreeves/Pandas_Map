#Importing needed libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import geopandas as gpd

#Loads data from specified path
#shp_file = "data\tl_2010_us_state10\tl_2010_us_state10.shp"
#map_frame = gpd.read_file(shp_file)

#Plots the United States
map_frame.plot()

#Loads csv file
frame = pd.read_csv('data\ACS_10_5YR_S0101\ACS_10_5YR_S0101_with_ann.csv')

#Selects columns we want
frame = frame[['Id', 'Geography', 'Total population']]

#Merge the .shp and .csv
merge = shp_file.set_index('NAME10').join(frame.set_index('Geography'))

#column to show on map
item = 'Total population'

#Setting the range of the choropleth
vmin, vmax = 500000, 37000000

#Figure and axes for matplotlib
fig, ax = plt.subplot(1, figsize=(15, 10))

#Creating map
merge.plot(column=item, cmap='Reds', linewidth=1.0 ax=ax, edgecolor='0.8')

#Removing the axis
ax.axis('off')

#Adding title
ax.set_title('Population of the United States', \
             fontdict={'fontsize': '30',
                       'fontweight': '5'})

#Annotation for sources
ax.annotate('Source: TIGER Census, 2010',
            xy=(0.1, 0.5), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize='8', color='#555555')

#Creating legend
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)

#Save
fig.savefig('US.png', dpi=300)
