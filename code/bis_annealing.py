import numpy as np 
from heap_algorithm import generate_permutations
from cities import cities_data

def earth_distance(lat1, lon1, lat2, lon2):
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
    output : float, distance in km
    '''
    distance = 0
    for i in range(len(itinerary)-1):
        lat1, lon1 = itinerary[i]['latitude'], itinerary[i]['longitude']
        lat2, lon2 = itinerary[i + 1]['latitude'], itinerary[i + 1]['longitude']
        distance += earth_distance(lat1, lon1, lat2, lon2)
    return distance



def greedy_optimization(city_list):
    # Generate permutations
    itineraries = []
    generate_permutations(city_list, len(city_list), itineraries)

    # Calculate the distance of all the itineraries
    distances = np.array([itinerary_distance(itinerary) for itinerary in itineraries])

    # Take the smallest one
    index = np.argmin(distances)

    #Output
    best_itinerary =  [city['name'] for city in itineraries[index]]
    return best_itinerary, distances[index]

def move_city_to_start(city_list, starting_city):
    city_index = next(index for (index, city) in enumerate(city_list) if city['name'] == starting_city)
    city = city_list.pop(city_index)
    city_list.insert(0, city)
    return city_list

def greedy_optimization_with_starting_point(city_list, starting_city):
    # Move starting city to start
    city_list = move_city_to_start(city_list, starting_city)
    
    # Generate permutations
    itineraries = []
    generate_permutations(city_list, len(city_list)-1, itineraries)

    # Calculate the distance of all the itineraries
    distances = np.array([itinerary_distance(itinerary) for itinerary in itineraries])

    # Take the smallest one
    index = np.argmin(distances)

    #Output
    best_itinerary =  [city['name'] for city in itineraries[index]]
    return best_itinerary, distances[index]


if __name__ == '__main__':
    # Recover french cities
    cities_france = [city for city in cities_data["cities"] if city.get("country") == "France"]
    
    # First we run the greedy algorithm
    greedy_itinerary, greedy_distance = greedy_optimization(cities_france)
    print(f'Best itinerary is {greedy_itinerary} with a total distance of {greedy_distance}' )