"""
%% The Mathematics of Host-Parasitoid Population Dynamics:
% This file provides several time-series trajectories of the logistic map
% for six different initial conditions.  Each trajectory is attracted to
% the nontrivial fixed point.  
% (This file creates Figure 2 of Section 1.3.)
"""

# Import libraries:
import numpy as np
import matplotlib.pyplot as plt

# Create a vector of six different initial conditions:
x0_vec = np.linspace(0.05, 0.9, 6)

# Create a string array of colors:
Color  = ['m', 'r', 'g', 'c', 'b', 'k']

# Loop through the six initial conditions, plotting the trajectory for each
# iteration: 
for i in range(len(x0_vec)):
    # Parameter:
    r = 2

    # Number of years:
    N = 10

    # Logistic map function:
    f = lambda x: r * x * (1 - x)

    # Initial populations:
    x0 = x0_vec[i]

    # Vector initialization and trajectory for loop:
    x = np.zeros(N + 1)
    x[0] = x0

    for t in range(N):
        x[t + 1] = r * x[t] * (1 - x[t])
        # equivalently: x[t + 1] = f(x[t])

    # Plot:
    plt.figure(1)
    plt.plot(range(N + 1), x, '-o', linewidth=3, color=Color[i])

    ax = plt.gca()
    ax.tick_params(labelsize=18)

    plt.title('Trajectories of the Logistic Map', fontsize=28)
    plt.xlabel(r'$t$', fontsize=22)
    plt.ylabel(r'$x_t$', fontsize=22)

    plt.legend([r'$x_0=.05$', r'$x_0=.22$', r'$x_0=.39$',
                r'$x_0=.56$', r'$x_0=.73$', r'$x_0=.90$'],
               fontsize=22)

    plt.ylim([0, 1])

# Apply grid lines to the figure:
plt.grid(True, which='both')
plt.minorticks_on()

plt.show()
