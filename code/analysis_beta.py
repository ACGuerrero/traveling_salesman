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
        metropolis_itinerary, distances[i] = metropolis_step(beta = beta, element = metropolis_itinerary, cost_func = itinerary_distance, dont_permute = dont_permute)
    print('Optimization completed')
    return distances

def run_optimization(cities, beta, steps, runs, dont_permute = 1):
    distances_all_steps = np.zeros((runs, steps))
    for i in range(runs):
        distances_all_steps[i]  = metropolis(cities, beta, steps, dont_permute=dont_permute)
    # Save data for each beta
    np.savetxt(f'data/beta_{beta:.2f}_steps_{steps:.0f}.dat', distances_all_steps, delimiter=',')
    print(f'Batch completed for beta = {beta}\n')

if __name__ == '__main__':
    # Read cities
    with open('data/cities.json', 'r') as f:
        cities_data = json.load(f)
    cities = np.array([city for city in cities_data['cities']])
    print(f'We are using {len(cities)} cities.')

    # ALGORITHM PARAMETERS
    steps = 3000
    betas = np.linspace(0.1, 1.1, 6)
    runs = 50

    # Create data if exists leave uncommented
    #for beta in betas: 
    #    run_optimization(cities, beta, steps, runs)

    # Grid setup
    cols = 3  # Number of columns in the grid
    rows = int(np.ceil(len(betas) / cols))  # Calculate the number of rows needed

    # Plotting
    fig, axs = plt.subplots(rows, cols, figsize=(15, 5*rows))
    
    for i, beta in enumerate(betas):
        distances_all_steps = np.loadtxt(f'data/beta_{beta:.2f}_steps_{steps:.0f}.dat', dtype=float, delimiter=',')
        avg_distance = np.mean(distances_all_steps, axis=0)  # Compute mean along axis 0
        final_distances = distances_all_steps[:, -1]
        row = i // cols
        col = i % cols
        ax = axs[row, col] if rows > 1 else axs[col]
        ax.plot(range(steps), distances_all_steps.T, color='gray', alpha=0.5)  # Transpose distances_all_steps
        ax.plot(range(steps), avg_distance, color='blue', label='Average')
        ax.set_title(fr'$\beta={beta:.2f}$')  # Title without final distance
        ax.set_ylabel('Distance')
        ax.set_xlabel('Steps')
        ax.legend(loc='upper left')

        # Add histogram
        ax_hist = ax.inset_axes([0.6, 0.6, 0.3, 0.3])   # Define position and size of histogram
        ax_hist.hist(final_distances, bins=10, alpha=0.5, color='orange')
        std_dev = np.std(final_distances)
        ax_hist.set_title(fr'$\sigma=${std_dev:.2f}, $\mu=${avg_distance[-1]:.2f}')  # Title with standard deviation


    # Hide empty subplots
    for i in range(len(betas), rows * cols):
        row = i // cols
        col = i % cols
        axs[row, col].axis('off')

    plt.tight_layout()
    plt.savefig('figures/beta_variation_grid_with_histogram.pdf')
    plt.show()
