"""
%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file shows the solutions to the ODE system using constant parasitism
% coupled with a density dependent host mortality.  We plot the explicit
% solution found in the text.  The solution is shown with respect to the 
% vulnerable period time variable tau. 
% (This file creates Figure 10 of Section 3.2)
"""

# Import libraries:
import numpy as np
import matplotlib.pyplot as plt

# Time Discretization:
T   = 1
tau = np.linspace(0, T, int(1e3))

# Parameter c Variation:
cd_vec = np.logspace(-1, 0, 2)

# Create two trajectories using a for loop:
for i in range(len(cd_vec)):
    
    # Parameters:
    cd = cd_vec[i]
    c  = 0.1
    R  = 2
    H  = 5
    P0 = 8  # (scalar P; avoid name clash with function below)
    
    # Solutions to basic parasitism with constant rate and host mortality:
    L = lambda t: (R*H) / (np.exp(c*P0*t) + cd*R*H*(np.exp(c*P0*t) - 1) / (c*P0))
    I = lambda t: (c*P0/cd) * np.log(1 + cd*R*H*(1 - np.exp(-c*P0*t)) / (c*P0))
    P = lambda t: P0 * np.ones_like(t)

    # Plot String:
    L_string = ['k', 'k:']
    I_string = ['r', 'r:']
    
    # MATLAB uses i=1..2 with linewidth = 5 - i -> 4, 3
    lw = 5 - (i + 1)

    # Plot:
    plt.figure(1)
    plt.plot(tau, L(tau), L_string[i], linewidth=lw)
    plt.plot(tau, I(tau), I_string[i], linewidth=lw)
    plt.gca().tick_params(labelsize=18)
    plt.title('Constant Attack with Host Mortality', fontsize=28)
    plt.xlabel(r'$\tau$ (time in vulnerable period)', fontsize=22)
    plt.ylabel(r'$L(\tau,t)$ and $I(\tau, t)$', fontsize=22)
    plt.legend([r'$L(\tau,t)$', r'$I(\tau,t)$'],
               loc='upper right', fontsize=22)
    if i == 0:
        plt.grid(True, which='both')
        plt.minorticks_on()

plt.show()
