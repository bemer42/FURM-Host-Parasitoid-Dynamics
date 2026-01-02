"""
%% The Mathematics of Host-Parasitoid Population Dynamics:
% This file provides a trajectory of the functional response model with 
% m = 1.  In this case, the model is neutrally stable and the trajectory is
% an example of a limit cycle. 
% (This file creates Figure 11 of Section 4.1.2)
"""

# Import Libraries:
import numpy as np
import matplotlib.pyplot as plt

# Parameters:
c = 0.1
k = 1
R = 2
T = 1

# Number of years:
N = 50

# Escape response:
f = lambda H, P: 1.0 / (1 + c * R * H * P * T)

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
    H[t + 1] = R * H[t] * f(H[t], P[t])
    P[t + 1] = k * R * H[t] * (1 - f(H[t], P[t]))

# Plot:
plt.figure(1, figsize=(12, 5))
plt.suptitle('Trajectory of Functional Response Model', fontsize=28)

# Time Series Plot:
plt.subplot(1, 2, 1)
plt.plot(range(N + 1), H, 'r-o', linewidth=3)
plt.plot(range(N + 1), P, 'b-o', linewidth=3)
plt.gca().tick_params(labelsize=18)
plt.title('Time Series Plot', fontsize=25)
plt.xlabel(r'$t$ (years)', fontsize=22)
plt.ylabel(r'$H_t$, $P_t$', fontsize=22)
plt.legend(['Hosts', 'Parasitoids'], loc='upper left', fontsize=22)
plt.grid(True, which='both')
plt.minorticks_on()

# Phase Plane Plot:
plt.subplot(1, 2, 2)
plt.plot(H, P, 'k-o', linewidth=3)
plt.plot(H0, P0, 'go', markersize=10, markeredgewidth=2)
plt.gca().tick_params(labelsize=18)
plt.title('Phase Plane Plot', fontsize=25)
plt.xlabel(r'$H_t$', fontsize=22)
plt.ylabel(r'$P_t$', fontsize=22)
plt.legend([r'$(H_t,P_t)$', r'$(H_0,H_0)$'], loc='upper right', fontsize=22)
plt.grid(True, which='both')
plt.minorticks_on()

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.show()
