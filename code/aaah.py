import numpy as np
import matplotlib.pyplot as plt
from tools import *
from optimization import *

def annealing(num_iterations, cities, T0, alpha, cooling_schedule):
    distances = np.zeros(num_iterations)
    best_distances = np.zeros(num_iterations)  # Array to store best distances
    current_itinerary = np.array(range(len(cities)))
    current_length = itinerary_cost(current_itinerary, cities)
    best_length = current_length
    Tcurr = T0

    for step in range(num_iterations):
        current_itinerary, current_length, Tcurr = simulated_annealing_step(cities, current_itinerary, Tcurr, T0, alpha, step, cooling_schedule)
        distances[step] = current_length
        
        if current_length < best_length:
            best_length = current_length
        best_distances[step] = best_length

    return distances, best_distances

def run_optimization(runs, num_iterations, cities, T0, alpha, cooling_schedule, cool_name):
    distances_all_steps = np.zeros((runs, num_iterations))
    best_distances_all_steps = np.zeros((runs, num_iterations))  # Array to store best distances

    for i in range(runs):
        distances, best_distances = annealing(num_iterations, cities, T0, alpha, cooling_schedule)
        distances_all_steps[i] = distances
        best_distances_all_steps[i] = best_distances
        print(f'Optimization {i} completed')

    # Save data for each beta
    np.savetxt(f'data/optimization_Ncities={len(cities)}_{cool_name}_alpha={alpha}_runs={num_iterations,}.dat', distances_all_steps, delimiter=',')
    np.savetxt(f'data/best_distances_Ncities={len(cities)}_{cool_name}_alpha={alpha}_runs={num_iterations,}.dat', best_distances_all_steps, delimiter=',')
    print(f'Batch completed for alpha={alpha}\n')

def cooling_comparisons():
    # We now define the parameters for our optimization
    steps = 1000
    T0 = 100
    alphas = [T0/steps, 100., 0.85, 0.85]
    cooling_schedules = [cooling_linear_m, cooling_logarithmic_m, cooling_exponential_m, cooling_quadratic_m]
    cooling_schedules_names = ['Linear', 'Logarithmic', 'Exponential', 'Quadratic']

    # We initialize. Current temp is the initial temp, current itinerary is just the initial order
    Tcurr = T0
    current_itinerary = np.array(range(N))
    current_length = itinerary_cost(current_itinerary, cities)

    plt.figure()
    # We apply the simulated annealing
    for i, cooling_schedule in enumerate(cooling_schedules):
        print(f'Now doing {cooling_schedules_names[i]} cooling schedule')
        distances = np.zeros(steps)
        best_distances = np.zeros(steps)  # Array to store best distances
        best_length = current_length
        
        for step in range(steps):
            current_itinerary, current_length, Tcurr = simulated_annealing_step(cities, current_itinerary, Tcurr, T0, alphas[i], step, cooling_schedule)
            distances[step] = current_length

            if current_length < best_length:
                best_length = current_length
            best_distances[step] = best_length

            if step % 100 == 0:
                print(f'Temperature is now {Tcurr}')
        
        plt.plot(np.array(range(steps)), distances, label=f'{cooling_schedules_names[i]} Distance')
        plt.plot(np.array(range(steps)), best_distances, label=f'{cooling_schedules_names[i]} Best Distance', linestyle='--')

        Tcurr = T0
        current_itinerary = np.array(range(N))
        current_length = itinerary_cost(current_itinerary, cities)

    plt.legend()
    plt.show()

if __name__ == '__main__':
    # Create cities
    N = 20
    np.random.seed(42) 
    cities = regular_polygon_vertices(apothem=0.4, num_sides=N, center=(0.5, 0.5))
    np.random.shuffle(cities) 

    # Cooling 
    schedules = [cooling_exponential_m, cooling_logarithmic_m, cooling_quadratic_m]
    names = ['Exponential', 'Logarithmic', 'Quadratic']
    colorsav = ['red', 'green', 'blue']
    colors = ['lightcoral', 'lightgreen', 'lightblue']
    k = 1
    color = colors[k]
    colorav = colorsav[k]
    cool_schedule = schedules[k]
    cool_name = names[k]
    alpha = 100

    # Run parameters
    num_iterations = 5000
    num_images = 200
    initial_temperature = 150

    # Create data
    runs = 50
    T0 = 100
    run_optimization(runs, num_iterations, cities, T0, alpha, cool_schedule, cool_name)

    distances_all_steps = np.loadtxt(f'data/optimization_Ncities={len(cities)}_{cool_name}_alpha={alpha}_runs={num_iterations,}.dat', dtype=float, delimiter=',')
    best_distances_all_steps = np.loadtxt(f'data/best_distances_Ncities={len(cities)}_{cool_name}_alpha={alpha}_runs={num_iterations,}.dat', dtype=float, delimiter=',')
    avg_distance = np.mean(distances_all_steps, axis=0)
    avg_best_distance = np.mean(best_distances_all_steps, axis=0)
    
    plt.figure()
    plt.plot(range(num_iterations), best_distances_all_steps.T, color=color, alpha=0.7)  # Transpose distances_all_steps
    plt.plot(range(num_iterations), avg_distance, color=colorav, label='Average Distance')
    plt.plot(range(num_iterations), avg_best_distance, color='black', linestyle='--', label='Average Best Distance')
    plt.axhline(y=itinerary_cost(range(N), regular_polygon_vertices(apothem=0.4, num_sides=N, center=(0.5, 0.5))), color='k', linestyle='-.', label='Optimal solution')
    plt.title(f'{cool_name} cooling, $\\alpha={alpha}$, {N} cities, {runs} runs')
    plt.xlabel('Iterations')
    plt.ylabel('Distance')
    plt.legend()

    plt.savefig(f'figures/optimization_Ncities={len(cities)}_{cool_name}_alpha={alpha}_runs={runs}.png')
    plt.close()