import numpy as np 
import matplotlib.pyplot as plt
import json
from heap import *
from optimization import *
from tools import *
from map import *

def metropolis(cities, beta, steps, dont_permute = 1):
    distances = np.zeros(steps)
    metropolis_itinerary = cities
    for i in range(steps):
        metropolis_itinerary, distances[i] = metropolis_step(beta = beta, element = metropolis_itinerary, cost_func = itinerary_distance, dont_permute = dont_permute)
    print('Optimization completed')
    return metropolis_itinerary, distances

if __name__ == '__main__':
    # Read cities
    with open('data/cities.json', 'r') as f:
        cities_data = json.load(f)
    cities = np.array([city for city in cities_data["cities"] if city.get("continent") == "Europe"])
    print(f'We are using {len(cities)} cities.')

    # ALGORITHM PARAMETERS
    steps = 10000
    beta = 2.3
    starting_city = 'Rome'
    cities = move_city_to_start(cities, starting_city)
    print(f'\nStaring city is {starting_city}')
    # CALLING ALGORITHM
    order, distances = metropolis(cities, beta, steps, dont_permute = 1)
    names = [city['name'] for city in order]
    print(names)


   # PLOTTING
    plt.figure(figsize=(12, 6))

    # Plot optimization distance
    plt.subplot(1, 2, 1)
    plt.plot(range(len(distances)), distances, label=r'$\beta=$'+f'{beta:.2f}')
    plt.title('Distance optimization')
    plt.ylabel('Mm')
    plt.xlabel('Steps')
    plt.legend()

    # Plot route
    plt.subplot(1, 2, 2)
    plt.title(f'Salesman starts at {starting_city}')
    plot_cities_route(order)

    plt.tight_layout()
    plt.savefig('figures/distance_optimization.pdf')
    plt.close()