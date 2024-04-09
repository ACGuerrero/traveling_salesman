import numpy as np
import matplotlib.pyplot as plt
from tools import *
from optimization import *

def ann_run(N, centers, side, num_iterations, initial_temperature, cooling_rate):# Example usage
    cities = clustered_cities(N, centers, side)
    distances = []
    M = N//1000
    T = initial_temperature
    beta = 1 / T
    current_itinerary, current_length = simulated_annealing(cities, 1, initial_temperature, cooling_rate)

    for i in range(num_iterations):
        current_itinerary, current_length = simulated_annealing_step(cities, current_itinerary, beta)
            if i % M == 0:
                distances.append(current_length)
        # Run one iteration of simulated annealing
        # Update beta
        T *= 1-cooling_rate
        beta = 1 / T
        if T<0.00001:
            T *= 100
            beta = 1 / T
            print('Temperature restarted')