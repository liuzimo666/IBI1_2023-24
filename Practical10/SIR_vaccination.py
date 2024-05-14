import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Define base variable
N = 10000  #  Total population
beta = 0.3  # Probability of infection
gamma = 0.05  # Probability of recovery

# Vaccination rates
vaccination_rates = np.linspace(0, 100, 11)

# Store the number of infected people per vaccination rate

I_arrs = {rate: [] for rate in vaccination_rates}

for rate in vaccination_rates:
    # The number of susceptible persons, infected persons and recovered persons is calculated based on the vaccination rate
    S = N * (1 - rate / 100)
    I = 1
    R = N - S - I

    # Creates an array to track changes in variables over time
    time = np.arange(1000)
    S_arr = [S] * len(time)
    I_arr = [I] * len(time)
    R_arr = [R] * len(time)

    for t in range(1, len(time)):
        new_infections = beta * S_arr[t-1] * I_arr[t-1] / N
        I_arr[t] = I_arr[t-1] + new_infections - gamma * I_arr[t-1]
        S_arr[t] = S_arr[t-1] - new_infections
        R_arr[t] = R_arr[t-1] + gamma * I_arr[t-1]
    I_arrs[rate] = I_arr

# Plot result
plt.figure(figsize=(6, 4), dpi=150)
for rate, I_arr in I_arrs.items():
    plt.plot(time, I_arr, label=f'{rate}% Vaccinated')

plt.xlabel('Time')
plt.ylabel('Number of Infected People')
plt.title('SIR Model with Vaccination')
plt.legend()
plt.show()
