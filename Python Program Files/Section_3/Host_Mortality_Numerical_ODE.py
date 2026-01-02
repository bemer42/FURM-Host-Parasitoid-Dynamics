"""
%% The Mathematics of Host-Parasitoid Population Dynamics:
% This file shows the solutions to the ODE system using constant parasitism
% coupled with a density dependent host mortality.  Although the solutions
% to the ODE can be found explicitly, we demonstrate how to solve the
% system numerically using Python's built-in ODE solver.  The solution is 
% shown with respect to the vulnerable period time variable tau. 
% (This file creates Figure 10 of Section 3.2)
"""

# Import libraries:
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Time Discretization:
T = 1
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
    P0 = 8

    # Define the initial conditions for the ODEs and place them in a vector:
    L_0 = R * H
    I_0 = 0
    P_0 = P0

    Y_0 = [L_0, I_0, P_0]

    # Define the right-hand side of the ODEs:
    def dYdtau(tau, Y):
        L, I, P = Y
        dLdtau = -c * L * P - cd * L**2
        dIdtau =  c * L * P
        dPdtau =  0.0
        return [dLdtau, dIdtau, dPdtau]

    # Call solve_ivp to solve the system (analogous to ode45):
    sol = solve_ivp(dYdtau, [0, T], Y_0, t_eval=tau, method='RK45', rtol=1e-6, atol=1e-9)

    L = sol.y[0]
    I = sol.y[1]
    P = sol.y[2]

    # Plot String:
    L_string = ['k', 'k:']
    I_string = ['r', 'r:']
    lw = 5 - (i + 1)  # Matches MATLAB’s linewidth(5-i)

    # Plot:
    plt.figure(1)
    plt.plot(tau, L, L_string[i], linewidth=lw)
    plt.plot(tau, I, I_string[i], linewidth=lw)
    plt.gca().tick_params(labelsize=18)
    plt.title('Constant Attack with Host Mortality', fontsize=28)
    plt.xlabel(r'$\tau$ (time in vulnerable period)', fontsize=22)
    plt.ylabel(r'$L(\tau,t)$ and $I(\tau,t)$', fontsize=22)
    plt.legend([r'$L(\tau,t)$', r'$I(\tau,t)$'],
               loc='upper right', fontsize=22)
    if i == 0:
        plt.grid(True, which='both')
        plt.minorticks_on()

plt.show()
