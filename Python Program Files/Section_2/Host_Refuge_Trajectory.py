"""
%% The Mathematics of Host-Parasitoid Population Dynamics:
% This file provides a trajectory of the host refuge model with two
% different values of alpha: alpha = .2 and alpha = .4.  The figure shows a
% comparison of the trajectories with a weak and strong refuge,
% respectively.
% (This file creates the right panel of Figure 7 of Section 2.3)
"""

# Import libraries:
import numpy as np
import matplotlib.pyplot as plt

# Parameter Variation:
alpha_vec = [0.2, 0.4]

# Create two trajectories using a for loop:
for i in range(len(alpha_vec)):

    # Parameters:
    alpha = alpha_vec[i]
    c = 0.1
    k = 1
    R = 2

    # Number of years:
    N = 50

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
        H[t + 1] = alpha * R * H[t] + (1 - alpha) * R * H[t] * f(P[t])
        P[t + 1] = k * (1 - alpha) * R * H[t] * (1 - f(P[t]))

    # Plot:
    plt.figure(1, figsize=(8, 10))
    plt.subplot(2, 1, i + 1)
    plt.plot(range(N + 1), H, 'r-o', linewidth=3)
    plt.plot(range(N + 1), P, 'b-o', linewidth=3)
    plt.gca().tick_params(labelsize=18)

    if i == 0:
        plt.title('Host Refuge Trajectories', fontsize=25)
        plt.ylim([0, 75])

    plt.xlabel(r'$t$ (years)', fontsize=22)
    plt.ylabel(r'$H_t$, $P_t$', fontsize=22)
    plt.legend(['Hosts', 'Parasitoids'], loc='upper right', fontsize=18)

    if i == 0:
        plt.text(0.01, 0.9,
                 fr'Weak Refuge - Limit Cycle ($\alpha = {alpha}$)',
                 fontsize=22, transform=plt.gca().transAxes)
    if i == 1:
        plt.text(0.2, 0.1,
                 fr'Strong Refuge - Stable ($\alpha = {alpha}$)',
                 fontsize=22, transform=plt.gca().transAxes)

    plt.grid(True, which='both')
    plt.minorticks_on()

plt.tight_layout()
plt.show()
