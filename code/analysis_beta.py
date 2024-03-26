import numpy as np 
import matplotlib.pyplot as plt
import json
from heap import *
from optimization import *
from tools import *

def metropolis(cities, beta, steps, dont_permute = 1):
    distances = np.zeros(steps)
    metropolis_itinerary = cities
    for i in range(steps):
        metropolis_itinerary = metropolis_step(beta = beta, element = metropolis_itinerary, cost_func = itinerary_distance, dont_permute = dont_permute)
        distances[i] = itinerary_distance(metropolis_itinerary)
    print('Optimization completed')
    return distances

if __name__ == '__main__':
    # Read cities
    with open('data/cities.json', 'r') as f:
        cities_data = json.load(f)
    cities = np.array([city for city in cities_data['cities']])
    print(f'We are using {len(cities)} cities.')

    # ALGORITHM PARAMETERS
    steps = 5000
    beta = 0.5
    starting_city = cities[1]['name']
    cities = move_city_to_start(cities, starting_city)
    print(f'\nStaring city is {starting_city}')
    betas = np.linspace(0.1,1.1,6)
    distances = np.zeros((len(betas),steps))
    # CALLING ALGORITHM
    for i, beta in enumerate(betas):
        distances[i] = metropolis(cities, beta, steps)


    # PLOTTING
    plt.figure()
    for i, beta in enumerate(betas):
        plt.plot(range(len(distances[i])),distances[i],label = r'$\beta=$'+f'{beta:.2f}')
    plt.title(r'Distance optimization for different $\beta$')
    plt.ylabel(r'Mm')
    plt.xlabel('Steps')
    plt.legend()
    plt.savefig('figures/beta_variation.pdf')