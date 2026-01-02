"""
%% The Mathematics of Host-Parasitoid Population Dynamics:
% This file constructs the Jury functions as functions of R for the
% Nicholson-Bailey model and plots them versus R.  The output is a graph
% that shows how the first two Jury functions are positive and the last
% Jury function is negative.  This shows that the coexistence fixed point
% of the Nicholson-Bailey is linearly unstable. 
% (This file creates the right panel of Figure 6 in Section 2.2.)
"""

# Import libraries:
import numpy as np
import matplotlib.pyplot as plt

# Discretizing R space: 
R = np.linspace(1, 7, int(1e4))

# Jury functions:
J1 = lambda R: np.log(R)
J2 = lambda R: 2 + np.log(R) * (R + 1) / (R - 1)
J3 = lambda R: 1 - np.log(R) * R / (R - 1)

# Plot: 
plt.figure(1)
plt.plot(R, J1(R), 'k', linewidth=5)
plt.plot(R, J2(R), 'r', linewidth=5)
plt.plot(R, J3(R), 'b', linewidth=5)

ax = plt.gca()
ax.tick_params(labelsize=18)
plt.title('Stability Analysis of N-B Model', fontsize=25)
plt.xlabel(r'$R$ (viable eggs per adult host)', fontsize=22)
plt.ylabel('Jury Functions', fontsize=22)
plt.legend(['Jury 1', 'Jury 2', 'Jury 3'],
           loc='upper left', fontsize=22)
plt.grid(True, which='both')
plt.minorticks_on()
plt.show()
