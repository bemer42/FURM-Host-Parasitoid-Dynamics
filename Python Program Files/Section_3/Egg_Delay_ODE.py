"""
%% The Mathematics of Host-Parasitoid Population Dynamics:
% This file solves the egg maturation delay ODE system given by Equations
% 91 and 92 of the text, with constant rates of parasitism and delay.
% (This file can essentially be used to solve Exercise 21.)
"""

# Import libraries:
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Time Discretization:
T = 1
tau = np.linspace(0, T, int(1e3))

# Parameters:
beta = 0.5
c    = 0.1
cr   = 1e1
R    = 2
H    = 5
P    = 8

# Define the initial conditions for the ODEs and place them in a vector:
L_0  = R * H
I_0  = 0
P0_0 = beta * P
P1_0 = (1 - beta) * P

Y_0 = [L_0, I_0, P0_0, P1_0]

# Define the right-hand side of the ODE system:
def dYdtau(tau, Y):
    L, I, P0, P1 = Y
    dLdtau  = -c * L * P1
    dIdtau  =  c * L * P1
    dP0dtau =  c * L * P1 - cr * P0
    dP1dtau = -c * L * P1 + cr * P0
    return [dLdtau, dIdtau, dP0dtau, dP1dtau]

# Solve the ODE system using solve_ivp (analogous to ode45):
sol = solve_ivp(dYdtau, [0, T], Y_0, t_eval=tau, method='RK45', rtol=1e-6, atol=1e-9)

# Extract solutions:
L  = sol.y[0]
I  = sol.y[1]
P0 = sol.y[2]
P1 = sol.y[3]

# Plot:
plt.figure(1)
plt.plot(tau, L, 'k', linewidth=5)
plt.plot(tau, I, 'r', linewidth=5)
plt.plot(tau, P0, 'b:', linewidth=5)
plt.plot(tau, P1, 'b', linewidth=5)
plt.gca().tick_params(labelsize=18)
plt.title('Constant Attack with Host Mortality', fontsize=28)
plt.xlabel(r'$\tau$ (time in vulnerable period)', fontsize=22)
plt.ylabel(r'$L(\tau,t)$ and $I(\tau,t)$', fontsize=22)
plt.legend([r'$L(\tau,t)$', r'$I(\tau,t)$', r'$P_0(\tau,t)$', r'$P_1(\tau,t)$'],
           loc='upper right', fontsize=22)
plt.grid(True, which='both')
plt.minorticks_on()
plt.show()
