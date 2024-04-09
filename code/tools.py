import numpy as np

def earth_distance(lat1, lon1, lat2, lon2):
    '''
    This function calculates the distance between two points
    on earth using spherical coordinates.

    Input: floats, latitudes and longitudes in degrees
    Output: float, distance in km
    '''
    # earth rayon
    R = 6371.0

    # To radians
    lat1, lon1, lat2, lon2 = np.radians([lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Forumula
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    return R * c

def itinerary_distance(itinerary):
    '''
    This function takes a list with the information of several cities and returns the total
    traveled distance.

    Input : list, of dictionaries with informations about cities
    output : float, distance in Mm
    '''
    distance = 0

    for i in range(len(itinerary)-1):
        lat1, lon1 = itinerary[i]['latitude'], itinerary[i]['longitude']
        lat2, lon2 = itinerary[i + 1]['latitude'], itinerary[i + 1]['longitude']
        distance += earth_distance(lat1, lon1, lat2, lon2)

    return distance/1000

def inter_city_distance(city1,city2):
    lat1, lon1 = city1['latitude'], city1['longitude']
    lat2, lon2 = city2['latitude'], city2['longitude']
    return earth_distance(lat1, lon1, lat2, lon2)


def move_city_to_start(city_list, starting_city):
    '''
    This function swaps two elements in the list of cities
    '''
    for i, city in enumerate(city_list):
        if city['name'] == starting_city:
            index = i
            break
    temp = city_list[i]
    city_list[i] = city_list[0]
    city_list[0] = temp
    return city_list

def manhattan_distance(points):
    tot = 0
    for i in range(len(points)-1) :
        tot += np.abs(points[i,0]-points[i+1,0])+np.abs(points[i,0]-points[i+1,1])
    return tot

def clustered_cities(N, centers, side):
    # As in the original paper, we use clustered cities
    num_centers = len(centers)
    cities_per_cluster = N // num_centers
    cities = []

    for center in centers:
        cluster_cities = np.random.rand(cities_per_cluster, 2) * side + np.array(center) - side / 2
        cities.extend(cluster_cities)

    # Add remaining cities at random, there's always a village in the middle of nowhere
    if len(cities) < N:
        remaining_cities = N - len(cities)
        random_cities = np.random.rand(remaining_cities, 2)
        cities.extend(random_cities)
    np.random.shuffle(cities)
    return np.array(cities)