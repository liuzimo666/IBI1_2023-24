import numpy as np
import matplotlib.pyplot as plt

# initialization parameter
N = 100  # sizing grid
population = np.zeros((N, N))  # Initializes the population array
outbreak = np.random.choice(range(N), 2)  # Pick a random point
population[outbreak[0], outbreak[1]] = 1  # Set this point to an infected state
beta = 0.3  # Infection probability
gamma = 0.05  # Recovery probability

# Draw initial state
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title("Initial State")
plt.show()

for t in range(100):  #100 time points
    # Find all the infected spots
    infected_points = np.argwhere(population == 1)
    for point in infected_points:
        # Infect 
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue 
                new_x, new_y = point[0] + dx, point[1] + dy
                if 0 <= new_x < N and 0 <= new_y < N:
                    if population[new_x, new_y] == 0 and np.random.rand() < beta:
                        population[new_x, new_y] = 1 
        # recovery
        if np.random.rand() < gamma:
            population[point[0], point[1]] = 2  # Set the infected person to recovery status
    
    # Plot
    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.title(f"Time Step {t}")
    plt.show()