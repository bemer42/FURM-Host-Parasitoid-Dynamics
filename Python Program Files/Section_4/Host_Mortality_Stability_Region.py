"""
%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file provides the stability region in (R,z) space for the host
% mortality semi-discrete model. 
% (This file creates the left panel of Figure 12 of Section 4.2)
"""

# Import Libraries:
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Parameter Vectors: 
N = 100
R_vec  = np.linspace(1.01, 5.0, N)
z_star = np.zeros_like(R_vec)

# Loop through values of R and solve for z*:
for i in range(len(R_vec)):
    R = R_vec[i]

    # Define equation to be solved: 
    # f(z) = R*(log(R) - z)/(R - exp(z)) - z - 1
    def f(z):
        return R * (np.log(R) - z) / (R - np.exp(z)) - z - 1.0

    # Define guess: 
    z_guess = 0.5 * np.log(R)
    
    # Solve for alpha^*
    sol = fsolve(f, z_guess, xtol=1e-6, maxfev=int(1e6))
    z_star[i] = sol[0]

# Plot boundary curves:
plt.figure(1)
plt.plot(R_vec, np.log(R_vec), 'k-', linewidth=3)
plt.plot(R_vec, z_star, 'k-.', linewidth=3)

ax = plt.gca()
ax.tick_params(labelsize=18)
plt.title('Host Mortality Stability Region', fontsize=25)
plt.xlabel(r'$R$ (viable eggs per adult host)', fontsize=22)
plt.ylabel(r'$z = c_d/kc$ (relative strength of host mortality to parasitism)',
           fontsize=22)
plt.legend([r'$z = \ln(R)$', r'$z = z^*$'], fontsize=22)

# Region labels at normalized (axes) coordinates:
ax.text(0.5, 0.5, 'No-Parasitoid Equilibrium', transform=ax.transAxes, fontsize=22)
ax.text(0.5, 0.6, 'Stable Coexistence', transform=ax.transAxes, fontsize=22)
ax.text(0.5, 0.7, 'Bounded Oscillations', transform=ax.transAxes, fontsize=22)

ax.grid(True, which='both')
ax.minorticks_on()
plt.show()
