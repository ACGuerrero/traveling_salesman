import numpy as np
import matplotlib.pyplot as plt
from tools import *
from optimization import *

def ann_run(N, centers, side, num_iterations, initial_temperature, cooling_rate, number_of_datapoints = 1000):# Example usage
    cities = clustered_cities(N, centers, side)
    distances = []
    restarts = []
    M = num_iterations//number_of_datapoints
    T = initial_temperature
    beta = 1 / T
    current_itinerary, current_length = simulated_annealing(cities, 1, initial_temperature, cooling_rate)
    best_itinerary = current_itinerary
    best_length = current_length
    for i in range(num_iterations):
        # Run the algorithm
        current_itinerary, current_length = simulated_annealing_step(cities, current_itinerary, beta)
        T *= 1-cooling_rate
        beta = 1 / T
        if T<0.00001:
            T *= 100
            beta = 1 / T
            print(f'Temperature restarted at {i}')
            restarts.append(i)

        # Save data and best run
        if current_length < best_length:
                best_itinerary = current_itinerary
                best_length = current_length
        if i % M == 0:
            distances.append(current_length)
            print(f'{len(distances)} points of data saved at {i}th iteration')
    return best_itinerary, np.array(distances), np.array(restarts)

if __name__ == '__main__':
    N = 50
    centers = [(0.25, 0.25), (0.5, 0.7), (0.75, 0.25), (0.75, 0.75)]   # Cluster centers
    side = 0.05  # Side length of each cluster
    num_iterations = 100000
    initial_temperature = 10
    number_of_datapoints = 1000
    cooling_rate = 0.0005
    best_run, distances, restarts = ann_run(N, centers, side, num_iterations, initial_temperature, cooling_rate, number_of_datapoints)
    M = num_iterations//number_of_datapoints
    print(f'Resrtarts at {restarts}')
    plt.figure()
    plt.plot(np.array(range(number_of_datapoints))*M,distances, 'k')
    for restart in restarts:
        plt.axvline(x=restart)
    plt.xlabel('Iteration')
    plt.ylabel('Tour distance')
    plt.title('Distance evolution with kicks')
    plt.savefig('figures/kicked_annealing.png')
    plt.savefig('figures/kicked_annealing.pdf')
    plt.show()
    plt.close()