import matplotlib.pyplot as plt
import json
from mpl_toolkits.basemap import Basemap
import numpy as np

# Define the Lambert Conformal Conic projection parameters for France
lon_0 = 5# Central longitude
lat_0 = 48 # Central latitude
lat_1 = 46
lat_2 = 50

# Create a Basemap instance
m = Basemap(
    width=480000,
    height=400000,
    projection='lcc',
    resolution='l',
    lat_0=lat_0,
    lon_0=lon_0,
    lat_1=lat_1,
    lat_2=lat_2
)

# Draw coastlines, countries, and states
m.drawcoastlines()
m.drawcountries()
m.drawstates()

# Draw parallels and meridians
m.drawparallels(range(40, 60, 2), labels=[1, 0, 0, 0])
m.drawmeridians(range(-10, 20, 2), labels=[0, 0, 0, 1])

with open('data/citiesfr.json', 'r') as f:
  citiesfr = json.load(f)

lat = [city['latitude'] for city in citiesfr['cities']]
long = [city['longitude'] for city in citiesfr['cities']]
names = [city['name'] for city in citiesfr['cities']]

lons, lats = m(long, lat)

m.scatter(lons, lats, marker = '.', color='r', zorder=5)
offset = 5000
for name, lon, lat in zip(names, lons, lats):
    plt.text(lon, lat+ offset, name, fontsize=8, ha='center', va='bottom', color='black')

if __name__ == "__main__":
  # Show the plot
  plt.title('Cities')
  plt.savefig('figures/france_map.pdf')
  plt.show()
  plt.close()
  print(lons, lats)