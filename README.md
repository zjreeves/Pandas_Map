# Pandas_Map
Creating a basic map using geopandas

# Why
For my project I wanted to make a map using no software with a GUI, like ArcMap or QGIS. We discussed how GIS is becoming, or already is, a data science. We also discussed how data scientists are using spatial data even though they have no GIS background. As a result, using this program I am able to import geospatial data, merge that data with a .csv file, create a plot showing the data, and then symbolized it all without using any other software. The result is supposed to be a very simple choropleth map of the United States showing each states population.
  
# How
First I downloaded both the .shp file for the United States and the .csv which had the population for each state. Next using geopandas I loaded united_states.shp. Using matplotlib, I plotted the United States shapefile. Then I loaded the .csv containing the population data. Using the set_index function, I joined both the .shp and the .csv together based on the name of the state. I then plotted the map showing the total population of each state. Next I eliminated the axes, changed the symbology to show red as a graduating color map. Finally I saved it.

# Usage 
This is a way to create very simple maps, very quickly. But it does not replace the more in depth analysis that can be done using ESRI's software. With more knowledge, you can perform more analysis using geopandas.

# References
Tutorial used as guide: http://darribas.org/gds15/content/labs/lab_03.html
Libraries: https://www.lfd.uci.edu/~gohlke/pythonlibs/
US State Map: TIGER Census
US Population Data: American Fact Finder



