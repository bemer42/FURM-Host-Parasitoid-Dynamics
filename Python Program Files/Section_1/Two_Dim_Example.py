"""
%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file provides a trajectory of the 2-D Example in Section 1.3. 
% The output of this program is Figure 2 in the text, which shows a
% trajectory of the dynamical system.  Two figures are created: 
%   - The first figure shows a time-series representation of the trajectory 
%     that clearly demonstrates the stability of the fixed point 
%     (x1*, y1*) = (3,11).  
%   - The second figure shows the phase plane representation of the
%     trajectory which also demonstrates the stability of the fixed point.
% (This file creates Figure 2 of Section 1.3.)
% This file also outputs the maximum eigenvalue for the Jacobian matrix
% evalated at each fixed point.
"""

# Import libraries:
import numpy as np
import matplotlib.pyplot as plt

# Number of years: 
N = 150

# Define the 2-D system functions:
f = lambda x, y: 5 + 0.25 * (x - y)
g = lambda x, y: 2 + 0.25 * x * (1 + y)

# Initial populations:
x0 = 5
y0 = 1

# Vector initialization: 
# (Allocate N+1 entries to store x_0,...,x_N and y_0,...,y_N.)
x = np.zeros(N + 1)
y = np.zeros(N + 1)
x[0] = x0
y[0] = y0

# Function iteration to create the trajectory:
for t in range(N):
    x[t + 1] = f(x[t], y[t])
    y[t + 1] = g(x[t], y[t])

# Time series plot: 
plt.figure(1, figsize=(12, 5))
plt.suptitle('Trajectory of 2D Example', fontsize=28)

ax1 = plt.subplot(1, 2, 1)
ax1.plot(range(N + 1), x, 'r-o', linewidth=3)
ax1.plot(range(N + 1), y, 'b-o', linewidth=3)
ax1.tick_params(labelsize=18)
ax1.set_title('Time Series Plot', fontsize=25)
ax1.set_xlabel(r'$t$', fontsize=22)
ax1.set_ylabel(r'$x_t$, $y_t$', fontsize=22)
ax1.legend([r'$x_t$', r'$y_t$'], loc='upper right', fontsize=22)
ax1.grid(True, which='both')
ax1.minorticks_on()

# Phase plane plot: 
ax2 = plt.subplot(1, 2, 2)
ax2.plot(x, y, 'k-o', linewidth=3)
ax2.plot(x0, y0, 'go', markersize=10, markeredgewidth=2)
ax2.tick_params(labelsize=18)
ax2.set_title('Phase Plane Plot', fontsize=25)
ax2.set_xlabel(r'$x_t$', fontsize=22)
ax2.set_ylabel(r'$y_t$', fontsize=22)
ax2.legend([r'$(x_t,y_t)$', r'$(x_0,y_0)$'], loc='upper right', fontsize=22)
ax2.grid(True, which='both')
ax2.minorticks_on()

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.show()

# Output the maximum eigenvalue of the Jacobian matrix evaluated at each 
# fixed point: 
J_1 = np.array([[0.25, -0.25],
                [3.0,   0.75]])
Evals_1 = np.linalg.eigvals(J_1)
rho_1   = np.max(np.abs(Evals_1))
print("rho_1 =", rho_1)

J_2 = np.array([[0.25, -0.25],
                [-0.75, 2.0]])
Evals_2 = np.linalg.eigvals(J_2)
rho_2   = np.max(np.abs(Evals_2))
print("rho_2 =", rho_2)
