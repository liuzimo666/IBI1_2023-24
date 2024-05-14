import numpy as np
import matplotlib.pyplot as plt

# Define base variable
N = 10000  # Total population
S = 9999  # Number of initial susceptibles
I = 1     # Initial number of infected persons
R = 0     # Number of initial recoveries
beta = 0.3  # probability of infection
gamma = 0.05  # Probability of recovery

# Creates an array to track changes in variables over time
time = np.arange(1000)  
S_arr = [S] * len(time)
I_arr = [I] * len(time)
R_arr = [R] * len(time)

for t in range(1, len(time)):
    # Infection of susceptible persons
    new_infections = beta * S_arr[t-1] * I_arr[t-1] / N
    I_arr[t] = I_arr[t-1] + new_infections - gamma * I_arr[t-1]
    S_arr[t] = S_arr[t-1] - new_infections
    R_arr[t] = R_arr[t-1] + gamma * I_arr[t-1]

# Plot result
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(time, S_arr, label='Susceptible')
plt.plot(time, I_arr, label='Infected')
plt.plot(time, R_arr, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model')
plt.legend()
plt.show()