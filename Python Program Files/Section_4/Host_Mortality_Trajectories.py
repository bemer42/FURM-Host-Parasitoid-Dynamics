"""
%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file provides a trajectory of the host mortality semi-discrete model
% for several values of the lumped parameter z. 
% (This file creates the right panel of Figure 12 of Section 4.2)
"""

# Import Libraries:
import numpy as np
import matplotlib.pyplot as plt

# Parameter Vector: 
z_vec = [0.8, 0.5, 0.23]

# Create three trajectories using a for loop:
plt.figure(1, figsize=(8, 12))
for i in range(3):
    
    # Parameters:
    c = 0.1
    z = z_vec[i]
    k = 1
    R = 2
    T = 1
    
    cd = z * c * k
    
    # Number of years:
    N = 50
    
    # Escape responses:
    # f(H,P) = exp(-c P T) / ( 1 + cd R H (-exp(-c P T) + 1) / (c P) )
    f = lambda H, P: np.exp(-c * P * T) / (1 + cd * R * H * (-np.exp(-c * P * T) + 1) / (c * P))
    # g(H,P) = (P / z) * log( 1 + cd R H (1 - exp(-c P T)) / (c P) )
    g = lambda H, P: (P / z) * np.log(1 + cd * R * H * (1 - np.exp(-c * P * T)) / (c * P))
    
    # Initial populations:
    H0 = 5
    P0 = 8
    
    # Vector initialization and tracjectory for loop:
    H = np.zeros(N + 1); H[0] = H0
    P = np.zeros(N + 1); P[0] = P0
       
    # Function iteration to create the trajectory:
    for t in range(N):
        H[t + 1] = R * H[t] * f(H[t], P[t])
        P[t + 1] = g(H[t], P[t])
    
    # Plot:
    plt.subplot(3, 1, i + 1)
    plt.plot(range(N + 1), H, 'r-o', linewidth=3)
    plt.plot(range(N + 1), P, 'b-o', linewidth=3)
    plt.gca().tick_params(labelsize=15)
    if i == 0:
        plt.title('Trajectories of Host Mortality Model', fontsize=25)
    plt.xlabel(r'$t$ (years)', fontsize=22)
    plt.ylabel(r'$H_t$, $P_t$', fontsize=22)
    plt.legend(['Hosts', 'Parasitoids'], loc='upper left', fontsize=22)
    plt.grid(True, which='both')
    plt.minorticks_on()

plt.tight_layout()
plt.show()
