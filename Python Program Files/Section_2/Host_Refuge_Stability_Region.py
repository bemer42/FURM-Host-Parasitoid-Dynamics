"""
%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file provides plots the stability region in (R,alpha) space for the
% host refuge model.
% (This file creates the left panel of Figure 7 of Section 2.3)
"""

# Import libraries:
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Parameter Vectors:
N = 100
R_vec  = np.linspace(1.01, 5.0, N)
a_star = np.zeros_like(R_vec)

# Loop through values of R and solve for alpha*:
for i in range(len(R_vec)):
    R = R_vec[i]

    # Define equation to be solved:
    def f(a):
        return (1 - a*R) * R / (R - 1) * np.log(((1 - a) * R) / (1 - a * R)) - 1.0

    # Define guess:
    a_guess = 0.9 / R

    # Solve for alpha^*
    sol = fsolve(f, a_guess, xtol=1e-6, maxfev=int(1e6))
    a_star[i] = sol[0]

# Plot boundary curves:
plt.figure(1)
plt.plot(R_vec, 1.0 / R_vec, 'k-', linewidth=3)
plt.plot(R_vec, a_star, 'k-.', linewidth=3)

ax = plt.gca()
ax.tick_params(labelsize=18)
plt.title('Host Refuge Stability Region', fontsize=25)
plt.xlabel(r'$R$ (viable eggs per adult host)', fontsize=22)
plt.ylabel(r'$\alpha$ (strength of host refuge)', fontsize=22)
plt.legend([r'$\alpha = 1/R$', r'$\alpha = \alpha^*$'], fontsize=18)

# Add region labels at normalized (axes) coordinates:
ax.text(0.5, 0.5, 'Bounded Oscillations', transform=ax.transAxes, fontsize=22)
ax.text(0.5, 0.6, 'Stable Equilibrium', transform=ax.transAxes, fontsize=22)
ax.text(0.5, 0.7, 'Unbounded Solutions', transform=ax.transAxes, fontsize=22)

ax.grid(True, which='both')
ax.minorticks_on()
plt.show()
