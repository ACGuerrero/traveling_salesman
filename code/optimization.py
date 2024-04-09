import numpy as np
from heap import *


def metropolis_step(beta, element, cost_func, dont_permute=0):
    '''
    This function performs a step of the Metropolis-Hastings algorithm.

    Input: float, np.array, function, and int indicating the
    number of elements not to shuffle
    Output: np.array, selected element
    '''
    # Create a shuffled copy of element and calculate cost
    new_element = np.copy(element)
    np.random.shuffle(new_element[dont_permute:])
    cost = cost_func(element)
    new_cost = cost_func(new_element)

    # Perform Metropolis-Hastings acceptance
    if new_cost < cost or np.random.rand() < np.exp(-beta * (new_cost - cost)):
        return new_element, new_cost
    else:
        return element, cost
    
def metropolis_step_swap(beta, element, cost_func, dont_permute=0):
    '''
    This function performs a step of the Metropolis-Hastings algorithm.

    Input: float, np.array, function, and int indicating the
    number of elements not to shuffle
    Output: np.array, selected element
    '''
    def swap_random(seq):
        idx = range(len(seq))
        i1, i2 = np.random.choice(idx, 2)
        seq[i1], seq[i2] = seq[i2], seq[i1]
    # Create a shuffled copy of element and calculate cost
    new_element = np.copy(element)
    swap_random(new_element[dont_permute:])
    cost = cost_func(element)
    new_cost = cost_func(new_element)

    # Perform Metropolis-Hastings acceptance
    if new_cost < cost or np.random.rand() < np.exp(-beta * (new_cost - cost)):
        return new_element
    else:
        return element
    
def metropolis_step_swap_square(beta, element, cost_func):
    '''
    This function performs a step of the Metropolis-Hastings algorithm.

    Input: float, np.array, function, and int indicating the
    number of elements not to shuffle
    Output: np.array, selected element
    '''
    def swap_random(seq):
        idx = range(len(seq))
        i1, i2 = np.random.choice(idx, 2)
        seq[i1], seq[i2] = seq[i2], seq[i1]
    # Create a shuffled copy of element and calculate cost
    new_element = np.copy(element)
    swap_random(new_element)
    cost = cost_func(element)
    new_cost = cost_func(new_element)

    # Perform Metropolis-Hastings acceptance
    if new_cost < cost or np.random.rand() < np.exp(-beta * (new_cost - cost)):
        return new_element
    else:
        return element


def greedy_optimization(elements,cost_func,dont_permute=0):
    '''
    This function performs the greedy optimization to obtain the best itinerary
    for the traveling salesman problem.

    Input: list, of dictionaries with information about cities
    Output: tuple, list with names of cities in order and float with distance in km
    '''
    # Generate permutations
    permutations = generate_permutations(elements, len(elements)-dont_permute)

    # Calculate the cost of all the permutations
    distances = np.array([cost_func(permutation) for permutation in permutations])

    # Take the smallest one
    index = np.argmin(distances)

    return permutations[index]


def smarter_greedy(elements, cost_func):
    '''
    This function starts at a city, selects the closest one, and repeats.
    '''
    N = len(elements)
    best_order = np.copy(elements)

    for i in range(N-1):
        for j in range(i+1, N-1):
            cost1 = cost_func(best_order[i], best_order[j])
            cost2 = cost_func(best_order[i], best_order[j+1])
            if cost2 < cost1:
            # Swap the closest city with the next position in the order
                temp = best_order[j]
                best_order[j] = best_order[j+1]
                best_order[j+1] = temp
                continue
    return best_order



def generate_random_itinerary(num_cities):
    # This just gives us a list with order
    itinerary = np.random.permutation(num_cities)
    return itinerary

def itinerary_cost(itinerary, cities):
    # The itinerary is the order !
    total_length = 0
    for i in range(len(itinerary) - 1):
        total_length += np.linalg.norm(cities[itinerary[i]] - cities[itinerary[i+1]]) # 
    return total_length

def acceptance_probability(delta_E, beta):
    return np.exp(-beta * delta_E)

def simulated_annealing_step(cities, current_itinerary, beta):

    num_cities = len(current_itinerary)
    new_itinerary = current_itinerary.copy()

    # We swap two elements randomly
    idx1, idx2 = np.random.choice(num_cities, 2, replace=False)
    new_itinerary[idx1], new_itinerary[idx2] = new_itinerary[idx2], new_itinerary[idx1]
    
    # We calculate costs
    current_length = itinerary_cost(current_itinerary, cities)
    new_length = itinerary_cost(new_itinerary, cities)

    # Acceptance condition
    delta_E = new_length - current_length
    if delta_E < 0 or np.random.rand() < acceptance_probability(delta_E, beta):
        return new_itinerary, new_length
    else:
        return current_itinerary, current_length



def simulated_annealing(cities, steps, T_init, cooling):
    '''
    This function will apply the stimulated annealing algorithm.
    However, it will save the best itinerary found, not only the most recent one !
    '''
    num_cities = len(cities)
    current_itinerary = np.array(range(num_cities))
    current_length = itinerary_cost(current_itinerary, cities)
    best_itinerary = current_itinerary.copy()
    best_length = current_length

    T = T_init
    beta = 1 / T
    for _ in range(steps) : 
        current_itinerary, current_length = simulated_annealing_step(cities, current_itinerary, beta)
        if current_length < best_length:
                best_itinerary = current_itinerary
                best_length = current_length

        # Cooling routine
        T *= 1-cooling
        beta = 1 / T

    return best_itinerary, best_length

def simulated_annealing_restart(cities, steps, T_init, cooling):
    '''
    This function will apply the stimulated annealing algorithm.
    However, it will save the best itinerary found, not only the most recent one !
    '''
    num_cities = len(cities)
    current_itinerary = np.array(range(num_cities))
    current_length = itinerary_cost(current_itinerary, cities)
    best_itinerary = current_itinerary.copy()
    best_length = current_length

    T = T_init
    beta = 1 / T
    for _ in range(steps) : 
        current_itinerary, current_length = simulated_annealing_step(cities, current_itinerary, beta)
        if current_length < best_length:
                best_itinerary = current_itinerary
                best_length = current_length

        # Cooling routine
        T *= 1-cooling
        beta = 1 / T
        if T<0.1:
            T = T_init
            beta = 1 / T
            print('Temperature restarted')

    return best_itinerary, best_length