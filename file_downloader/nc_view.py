#Minor edits, but script sourced from:
#https://rabernat.github.io/research_computing/intro-to-basemap.html

import netCDF4
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook
import sys

filename = sys.argv[1]
url=filename

plt.figure()

# Extract the Total Precipitate Water data and the longitudes and latitudes
file = netCDF4.Dataset(url)
lat  = file.variables['latArr'][:]
lon  = file.variables['lonArr'][:]
data = file.variables['tpwGrid'][:,:]
file.close()

# Plot the field using Basemap.  Start with setting the map
# projection using the limits of the lat/lon data itself:
fig=plt.figure(figsize=(12, 8) )

# Miller projection:
m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), \
  urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
  resolution='c')


# convert the lat/lon values to x/y projections.

x, y = m(*np.meshgrid(lon,lat))

# plot the field using the fast pcolormesh routine 
# set the colormap to jet.

m.pcolormesh(x,y,data,shading='flat',cmap=plt.cm.jet)
m.colorbar(location='right')

# Add a coastline and axis values.

m.drawcoastlines()
m.fillcontinents()
m.drawmapboundary()
m.drawparallels(np.arange(-90.,90.,30.),labels=[1,0,0,0])
m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])

# Add a colorbar and title, and then show the plot.

plt.title('')
plt.savefig(sys.argv[1] + '.png')
#plt.show()
