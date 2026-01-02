"""
%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file graphs a time series trajectory of the Nicholson-Bailey Model.
% (This file creates the left panel of Figure 6 in Section 2.2.)
"""

# Import libraries:
import numpy as np
import matplotlib.pyplot as plt

# Model Parameters: 
c = 0.1
R = 2
k = 1

# Number of years: 
N = 20

# Escape response:
f = lambda P: np.exp(-c * P)

# Initial populations:
H0 = 5
P0 = 8

# Vector initialization: 
H = np.zeros(N + 1)
P = np.zeros(N + 1)
H[0] = H0
P[0] = P0

# Function iteration to create the trajectory:
for t in range(N):
    H[t + 1] = R * H[t] * f(P[t])
    P[t + 1] = k * R * H[t] * (1 - f(P[t]))

# Time Series Plot: 
plt.figure(1)
plt.plot(range(N + 1), H, 'r-o', linewidth=3)
plt.plot(range(N + 1), P, 'b-o', linewidth=3)
plt.gca().tick_params(labelsize=18)
plt.title('Trajectory of Nicholson-Bailey Model', fontsize=25)
plt.xlabel(r'$t$ (years)', fontsize=22)
plt.ylabel(r'$H_t$, $P_t$', fontsize=22)
plt.legend(['Hosts', 'Parasitoids'], loc='upper left')
plt.grid(True, which='both')
plt.minorticks_on()

# Phase Plane Plot:
plt.figure(2)
plt.plot(H, P, 'k-o', linewidth=3)
plt.plot(H0, P0, 'go', markersize=10, markeredgewidth=2)
plt.gca().tick_params(labelsize=18)
plt.title('Trajectory of Nicholson-Bailey Model', fontsize=25)
plt.xlabel(r'$H_t$ (hosts)', fontsize=22)
plt.ylabel(r'$P_t$ (parsitoids)', fontsize=22)
plt.legend([r'$(H_t,P_t)$', r'$(H_0,P_0)$'], loc='upper left')
plt.grid(True, which='both')
plt.minorticks_on()

plt.show()
