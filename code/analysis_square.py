import numpy as np
import matplotlib.pyplot as plt
from tools import *
from optimization import *
import imageio

def create_gif(N, centers, side, num_iterations, initial_temperature, cooling_rate):# Example usage
    points = clustered_cities(N, centers, side)
    frames = []
    fig, ax = plt.subplots()
    M = 500
    T = initial_temperature
    beta = 1 / T
    current_itinerary, current_length = simulated_annealing(points, 1, initial_temperature, cooling_rate)

    for i in range(num_iterations):
        if i % M == 0:
            ax.clear()
            ax.plot(points[:, 0], points[:, 1], 'ko')
            ax.plot(points[current_itinerary, 0], points[current_itinerary, 1], 'k-')
            ax.set_title(f"Iteration: {i}, Length: {current_length:.2f}, Beta: {beta:.2f}")
            ax.set_xticks([])
            ax.set_yticks([])
            plt.tight_layout()
            fig.canvas.draw()
            frame = np.array(fig.canvas.renderer.buffer_rgba())
            frames.append(frame)
            print(f'Iteration {i}. Current T={T}. Current beta ={beta}')

        # Run one iteration of simulated annealing
        current_itinerary, current_length = simulated_annealing_step(points, current_itinerary, beta)
        # Update beta
        T *= 1-cooling_rate
        beta = 1 / T
        if T<0.00001:
            T *= 100
            beta = 1 / T
            print('Temperature restarted')

    # Save frames as a GIF
    imageio.mimsave('tour_evolution.gif', frames, fps=30)

if __name__ == '__main__' :
    # Example usage
    N = 50
    centers = [(0.25, 0.25), (0.5, 0.7), (0.75, 0.25), (0.75, 0.75)]   # Cluster centers
    side = 0.05  # Side length of each cluster

    num_iterations = 100000
    initial_temperature = 100
    cooling_rate = 0.0005

    create_gif(N, centers, side, num_iterations, initial_temperature, cooling_rate)