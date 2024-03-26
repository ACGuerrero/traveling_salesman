import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

def plot_cities_map(cities):
    lat = [city['latitude'] for city in cities]
    lon = [city['longitude'] for city in cities]
    names = [city['name'] for city in cities]

    m = Basemap(
        projection='merc',
        llcrnrlat=min(lat) - 1,
        urcrnrlat=max(lat) + 1,
        llcrnrlon=min(lon) - 1,
        urcrnrlon=max(lon) + 1,
        resolution='i',
        epsg=4326
    )

    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    m.drawparallels(np.arange(-90., 91., 1.), labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(-180., 181., 1.), labels=[0, 0, 0, 1])

    x, y = m(lon, lat)
    m.scatter(x, y, marker='.', color='r', zorder=5)

    offset = 5000
    for name, lon, lat in zip(names, lon, lat):
        x, y = m(lon, lat)
        plt.text(x, y, name, fontsize=8, ha='center', va='bottom', color='black')

def plot_cities_route(cities):
    lat = [city['latitude'] for city in cities]
    lon = [city['longitude'] for city in cities]

    m = Basemap(
        projection='merc',
        llcrnrlat=min(lat) - 1,
        urcrnrlat=max(lat) + 1,
        llcrnrlon=min(lon) - 1,
        urcrnrlon=max(lon) + 1,
        resolution='i',
        epsg=4326
    )

    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()

    x, y = m(lon, lat)
    m.scatter(x, y, marker='.', color='r', zorder=5)

    for i in range(len(cities) - 1):  # Iterate up to the second to last city
        lon1, lat1 = cities[i]['longitude'], cities[i]['latitude']
        lon2, lat2 = cities[i + 1]['longitude'], cities[i + 1]['latitude']  # Corrected order
        m.drawgreatcircle(lon1, lat1, lon2, lat2, linewidth=2, color='b')

    plt.title('Cities with Route')

if __name__ == '__main__':
  # Example usage:
  cities = [{'name': 'Besancon', 'latitude': 47.238, 'longitude': 6.0244},
            {'name': 'Nancy', 'latitude': 48.6921, 'longitude': 6.1844},
            {'name': 'Paris', 'latitude': 48.8566, 'longitude': 2.3522},
            {'name': 'Dijon', 'latitude': 47.322, 'longitude': 5.0415},
            {'name': 'Mulhouse', 'latitude': 47.7508, 'longitude': 7.3359},
            {'name': 'Strasbourg', 'latitude': 48.5734, 'longitude': 7.7521}]

  plt.figure()
  plot_cities_map(cities)
  plot_cities_route(cities)
  plt.show()
  plt.close()