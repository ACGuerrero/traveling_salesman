import numpy as np 
from good_heap import *
from cities import cities_data

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
    output : float, distance in km
    '''
    distance = 0

    for i in range(len(itinerary)-1):
        lat1, lon1 = itinerary[i]['latitude'], itinerary[i]['longitude']
        lat2, lon2 = itinerary[i + 1]['latitude'], itinerary[i + 1]['longitude']
        distance += earth_distance(lat1, lon1, lat2, lon2)

    return distance


def greedy_optimization(city_list):
    '''
    This function performs the greedy optimization to obtain the best itinerary
    for the traveling salesman problem.

    Input: list, of dictionaries with information about cities
    Output: tuple, list with names of cities in order and float with distance in km
    '''
    # Generate permutations
    itineraries =generate_permutations(city_list, len(city_list))

    # Calculate the distance of all the itineraries
    distances = np.array([itinerary_distance(itinerary) for itinerary in itineraries])

    # Take the smallest one
    index = np.argmin(distances)

    #Output
    best_itinerary =  [city['name'] for city in itineraries[index]]
    return best_itinerary, distances[index]


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

def greedy_optimization_with_starting_point(city_list, starting_city):
    # Move starting city to start
    city_list = np.flip(move_city_to_start(city_list, starting_city))
    
    # Generate permutations
    itineraries =generate_permutations(city_list, len(city_list)-1)

    # Calculate the distance of all the itineraries
    distances = np.array([itinerary_distance(itinerary) for itinerary in itineraries])

    # Take the smallest one
    index = np.argmin(distances)

    #Output
    best_itinerary =  np.flip(np.array([city['name'] for city in itineraries[index]]))
    return best_itinerary, distances[index]


def metropolis_step(beta,itinerary):
    '''
    This function performs a step of the Metropolis-Hastings algorithm.

    Input: float and np.array, beta parameter and itinerary
    Output: np.array, selected itinerary
    '''
    distance = itinerary_distance(itinerary)
    new_itinerary = np.random.permutation(itinerary)
    new_distance = itinerary_distance(new_itinerary)

    if  new_distance < distance:
        return new_itinerary
    else:
        boltzmann_factor = np.exp(-beta*new_distance)
        r = np.random.rand()
        if boltzmann_factor > r :
            return new_itinerary
        else:
            return itinerary

def metropolis_step_with_starting_point(beta,itinerary):
    '''
    This function performs a step of the Metropolis-Hastings algorithm.

    Input: float and np.array, beta parameter and itinerary
    Output: np.array, selected itinerary
    '''
    distance = itinerary_distance(itinerary)
    rest = itinerary[1:]
    newrest = np.random.permutation(rest)
    new_itinerary = itinerary
    new_itinerary[1:] = newrest
    new_distance = itinerary_distance(new_itinerary)

    if  new_distance < distance:
        return new_itinerary
    else:
        boltzmann_factor = np.exp(-beta*(new_distance-distance))
        r = np.random.rand()
        if boltzmann_factor > r :
            return new_itinerary
        else:
            return itinerary
        
def smarter_greedy():
    '''
    This one starts at a city, selects the closest one, and repeats
    '''
    return None


if __name__ == '__main__':
    # Recover french cities
    cities_europe = np.array([city for city in cities_data["cities"] if city.get("continent") == "Europe"])[0:8]
    cities_france = np.array([city for city in cities_data["cities"] if city.get("country") == "France"])
    using = cities_europe

    # First we run the Metropolis Hastings
    steps = 100
    beta = 0.039
    hastings_itinerary = using
    for i in range(steps):
        hastings_itinerary = metropolis_step(beta,hastings_itinerary)
    hastings_distance = itinerary_distance(hastings_itinerary)

    hastings_itinerary_names = [city['name'] for city in hastings_itinerary]
    print('\n**********************************\n')
    print(f'\nHastings itinerary is {hastings_itinerary_names} with a total distance of {hastings_distance}\n' )


    # Now we run the greedy algorithm
    #greedy_itinerary, greedy_distance = greedy_optimization(using)
    #print(f'Greedy itinerary is {greedy_itinerary} with a total distance of {greedy_distance}\n' )

    # Now with Starting point !

    starting_city = 'Dijon'
    print('\n**********************************\n')

    print('\nStaring city is '+starting_city)

    #greedy_itinerary1, greedy_distance1 = greedy_optimization_with_starting_point(using,starting_city)
    #print(f'\nWe greedily get {greedy_itinerary1} with a total distance of {greedy_distance1}\n' )

    # Now Hastings
    steps = 10000
    beta = 0.0001
    hastings_itinerary = move_city_to_start(using, starting_city)
    for i in range(steps):
        hastings_itinerary = metropolis_step_with_starting_point(beta,hastings_itinerary)
    hastings_distance = itinerary_distance(hastings_itinerary)

    hastings_itinerary_names = [city['name'] for city in hastings_itinerary]

    print(f'\nHastings itinerary is {hastings_itinerary_names} with a total distance of {hastings_distance}\n' )
