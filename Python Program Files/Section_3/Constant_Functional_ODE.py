"""
%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file shows the solutions to the ODE systems using constant and
% functional response parsitism for different values of the attack
% parameter c.  The output is two figures of both models that shows the
% solution during the vulnerable period. 
% (This file creates Figure 9 of Section 3.1.1)
"""

# Import libraries:
import numpy as np
import matplotlib.pyplot as plt

# Time Discretization:
T   = 1
tau = np.linspace(0, T, int(1e3))

# Parameter c variation:
c_vec = np.log10(np.logspace(-1, 0, 2))  # placeholder to mirror MATLAB? (See below)
# NOTE: The MATLAB uses: c_vec = logspace(-1,0,2);
# In Python, that's simply:
c_vec = np.logspace(-1, 0, 2)

# Create two trajectories using a for loop:
for i in range(len(c_vec)):
    
    # Parameters:
    c = c_vec[i]
    R = 2
    H = 5
    P = 8
    
    # Solutions to Basic Parasitism with Constant Rate:
    L1 = lambda tau: R * H * np.exp(-c * P * tau)
    I1 = lambda tau: R * H * (1 - np.exp(-c * P * tau))
    P1 = lambda tau: P * np.ones_like(tau)
    
    # Solutions to Basic Parasitism with Functional Rate:
    L2 = lambda tau: (R * H) / (1 + c * R * H * P * tau)
    I2 = lambda tau: R * H * (1 - 1 / (1 + c * R * H * P * tau))
    P2 = lambda tau: P * np.ones_like(tau)
    
    # Plot String:
    L_string = ['k', 'k:']
    I_string = ['r', 'r:']
    
    # MATLAB uses i = 1,2 and linewidth = 5 - i -> 4 then 3
    lw = 4 - i

    # Plot:
    plt.figure(1, figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(tau, L1(tau), L_string[i], linewidth=lw)
    plt.plot(tau, I1(tau), I_string[i], linewidth=lw)
    plt.gca().tick_params(labelsize=8)
    plt.title('Constant Attack', fontsize=28)
    plt.xlabel(r'$\tau$ (time in vulnerable period)', fontsize=22)
    plt.ylabel(r'$L(\tau,t)$ and $I(\tau, t)$', fontsize=22)
    plt.legend([r'$L(\tau,t)$', r'$I(\tau,t)$'], loc='upper right', fontsize=22)
    if i == 0:
        plt.grid(True, which='both')
        plt.minorticks_on()
    
    plt.subplot(1, 2, 2)
    plt.plot(tau, L2(tau), L_string[i], linewidth=lw)
    plt.plot(tau, I2(tau), I_string[i], linewidth=lw)
    plt.gca().tick_params(labelsize=18)
    plt.title('Functional Response Attack', fontsize=28)
    plt.xlabel(r'$\tau$ (time in vulnerable period)', fontsize=22)
    plt.ylabel(r'$L(\tau,t)$ and $I(\tau, t)$', fontsize=22)
    plt.legend([r'$L(\tau,t)$', r'$I(\tau,t)$'], loc='upper right', fontsize=22)
    if i == 0:
        plt.grid(True, which='both')
        plt.minorticks_on()

plt.tight_layout()
plt.show()
