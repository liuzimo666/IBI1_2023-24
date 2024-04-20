import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#Define the space size and time step
n, m = 100, 100  
dt = 0.1  
dx = 1  
iterations = 1000  

# Initialize S, I, R
S = np.ones((n, m))
I = np.zeros((n, m))
R = np.zeros((n, m))
# Place an infected person in the center
I[n//2, m//2] = 1

# Define disease transmission parameters
beta = 0.3  
gamma = 0.05  

for _ in range(iterations):
    # calculate S, I, R
    S_new = np.roll(S, 1, axis=(0, 1)) * np.roll(I, -1, axis=(0, 1)) / (dx * dx)
    I_new = I + dt * (-beta * S * I + gamma * I)
    R_new = np.roll(R, -1, axis=(0, 1)) * np.roll(I, 1, axis=(0, 1)) / (dx * dx)
    
    S = S_new
    I = I_new
    R = R_new

# plot
plt.figure(figsize=(10, 10))
plt.imshow(I, cmap='viridis', interpolation='none')
plt.title('2D SIR Model')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.colorbar()
plt.show()