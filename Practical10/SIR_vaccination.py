import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Parameters
N = 1000  # Total population
I0 = 1    # Initial number of infected
R0 = 0    # Initial number of recovered
V0 = 0.1 * N  # Initial number of vaccinated (10% of the population)
S0 = N - I0 - R0 - V0  # Initial number of susceptible
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate

# Time steps
t_max = 100
dt = 1
t = np.arange(0, t_max, dt)
# write the name
# Initialize arrays
S = np.zeros(t_max)
I = np.zeros(t_max)
R = np.zeros(t_max)
V = np.zeros(t_max)

# Set initial conditions
S[0] = S0
I[0] = I0
R[0] = R0
V[0] = V0

# SIRV model
for i in range(t_max - 1):
    dSdt = -beta * S[i] * I[i] / N  # Rate of change of susceptible
    dIdt = beta * S[i] * I[i] / N - gamma * I[i]  # Rate of change of infected
    dRdt = gamma * I[i]  # Rate of change of recovered
    dVdt = 0  # Rate of change of vaccinated (constant)
    
    # Update populations
    S[i + 1] = S[i] + dSdt * dt
    I[i + 1] = I[i] + dIdt * dt
    R[i + 1] = R[i] + dRdt * dt
    V[i + 1] = V[i] + dVdt * dt

# Plot the results
plt.plot(t, S, label='Susceptible', color=cm.viridis(20))
plt.plot(t, I, label='Infected', color=cm.viridis(50))
plt.plot(t, R, label='Recovered', color=cm.viridis(80))
plt.plot(t, V, label='Vaccinated', color=cm.viridis(110))
plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.legend()
plt.show()
