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
        i1, i2 = np.random.sample(idx, 2)
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

