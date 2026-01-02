"""
%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file solves the egg maturation delay ODE system given by Equations
% 91 and 92 of the text, with constant rates of parasitism and delay.
% (This file can essentially be used to solve Exercise 21.)
"""

# Import libraries:
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Vulnerable Period Time Discretization:
T   = 1
tau = np.linspace(0, T, int(1e3))

# Number of years:
N = 50

# Parameters:
beta = 0.5
c    = 0.1
cr   = 1e0
R    = 2
k    = 1

# Initial populations:
H_0 = 5
P_0 = 8

# Vector initialization:
H = np.zeros(N + 1)
P = np.zeros(N + 1)
H[0] = H_0
P[0] = P_0

# Function iteration to create the trajectory:
for t in range(N):

    # Define the initial conditions for the ODEs and place them in a vector:
    L_0  = R * H[t]
    I_0  = 0
    P0_0 = beta * P[t]
    P1_0 = (1 - beta) * P[t]

    Y_0 = [L_0, I_0, P0_0, P1_0]

    # Define the right-hand side of the ODEs and a vector function:
    # dL/dtau  = -c*L*P1
    # dI/dtau  =  c*L*P1
    # dP0/dtau =  c*L*P1 - cr*P0
    # dP1/dtau = -c*L*P1 + cr*P0
    def dYdtau(tau_, Y):
        L, I, P0, P1 = Y
        dLdtau  = -c * L * P1
        dIdtau  =  c * L * P1
        dP0dtau =  c * L * P1 - cr * P0
        dP1dtau = -c * L * P1 + cr * P0
        return [dLdtau, dIdtau, dP0dtau, dP1dtau]

    # Call the built-in ODE solver (ode15s analog -> BDF) to solve the system:
    sol = solve_ivp(dYdtau, [0, T], Y_0, t_eval=tau, method='BDF', rtol=1e-6, atol=1e-9)

    L  = sol.y[0]
    I  = sol.y[1]
    P0 = sol.y[2]
    P1 = sol.y[3]

    # Define the next year update values for H_t and P_t:
    H[t + 1] = L[-1]
    P[t + 1] = k * I[-1]

# Plot: 
plt.figure(1, figsize=(12, 5))
plt.suptitle('Trajectory of Egg Maturation Delay Model', fontsize=28)

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

# Phase plane plot: 
plt.subplot(1, 2, 2)
plt.plot(H, P, 'k-o', linewidth=3)
plt.plot(H_0, P_0, 'go', markersize=10, markeredgewidth=2)
plt.gca().tick_params(labelsize=18)
plt.title('Phase Plane Plot', fontsize=25)
plt.xlabel(r'$H_t$', fontsize=22)
plt.ylabel(r'$P_t$', fontsize=22)
# Keeping legend text consistent with the MATLAB script:
plt.legend([r'$(H_t,P_t)$', r'$(H_0,H_0)$'], loc='upper right', fontsize=22)
plt.grid(True, which='both')
plt.minorticks_on()

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.show()
