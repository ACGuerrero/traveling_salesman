import numpy as np 
from good_heap import *
from cities import cities_data
import matplotlib.pyplot as plt


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

def metropolis_step_with_starting_point(beta, itinerary):
    '''
    This function performs a step of the Metropolis-Hastings algorithm.

    Input: float and np.array, beta parameter and itinerary
    Output: np.array, selected itinerary
    '''
    distance = itinerary_distance(itinerary)
    
    # Make a deep copy of the itinerary
    new_itinerary = np.copy(itinerary)
    
    # Shuffle elements starting from the second index
    rest = new_itinerary[1:]
    np.random.shuffle(rest)
    
    # Assign shuffled elements back to the itinerary
    new_itinerary[1:] = rest
    
    new_distance = itinerary_distance(new_itinerary)
    print(distance, new_distance)

    if new_distance < distance:
        return new_itinerary
    else:
        boltzmann_factor = np.exp(-beta * (new_distance - distance))
        r = np.random.rand()
        if boltzmann_factor > r:
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
    cities_europe = np.array([city for city in cities_data["cities"] if city.get("continent") == "Europe"])
    cities_france = np.array([city for city in cities_data["cities"] if city.get("country") == "France"])
    cities = np.array([city for city in cities_data['cities']])
    using = cities
    np.random.shuffle(using)

    starting_city = 'Beyrouth'
    steps = 500
    beta = 10
    print(f'\nStaring city is {starting_city}')

    # Now Hastings
    distances1 = np.zeros(steps)
    distances2 = np.zeros(steps)
    metropolis_itinerary = move_city_to_start(using, starting_city)
    for i in range(steps):
        metropolis_itinerary = metropolis_step_with_starting_point(beta,metropolis_itinerary)
        distances1[i] = itinerary_distance(metropolis_itinerary)/1000
    metropolis_distance = itinerary_distance(metropolis_itinerary)
    print(distances1)

    # First we run the Metropolis metropolis
    metropolis_itinerary = using
    for i in range(steps):
        metropolis_itinerary = metropolis_step(beta,metropolis_itinerary)
        distances2[i] = itinerary_distance(metropolis_itinerary)/1000
    metropolis_distance = itinerary_distance(metropolis_itinerary)

    metropolis_itinerary_names = [city['name'] for city in metropolis_itinerary]

    print(f'\nmetropolis itinerary is {metropolis_itinerary_names} with a total distance of {metropolis_distance}\n' )

    plt.plot(range(len(distances1)),distances1,label = 'with starting .')
    plt.plot(range(len(distances2)),distances2, label = 'no starting .')
    plt.legend()
    plt.savefig('figures/distances.png')