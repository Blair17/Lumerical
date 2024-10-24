import os
import numpy as np
import matplotlib.pyplot as plt
import glob
import pandas as pd
from matplotlib import cm
from matplotlib.cm import ScalarMappable
from matplotlib.colors import ListedColormap
from scipy.interpolate import UnivariateSpline
import statsmodels.api as sm
from scipy.optimize import curve_fit

voltage_array = np.linspace(0,35,9)

diff_array = []
first = True
for i in range(len(phase_array)):
    if first == True:
        diff_array.append(0)
        first = False
    else:
        diff = phase_array[i] - phase_array[0]
        diff_array.append(diff)

y = [1]
x = [21.2]

# colors = ["white", "turquoise", "lightseagreen", "teal", "darkslategrey"]


### Sigmoid fitting ###
initial_guess = [1, np.median(voltage_array), 1, 0]
params, covariance = curve_fit(sigmoid, voltage_array, diff_array, p0=initial_guess)

x_fit = np.linspace(min(voltage_array), max(voltage_array), 1000)
y_fit = sigmoid(x_fit, *params)

fig2, ax = plt.subplots(figsize=[10,7])
# ax.plot(voltage_array, diff_array, lw=3, color='darkslategrey')
ax.plot(x_fit, y_fit, lw=3, color='darkslategrey')

ax.axhline(y=1, xmin=0, xmax=0.6, color='turquoise', lw=3, linestyle='--')
ax.axvline(x=x, ymin=0, ymax=0.52, color='turquoise', lw=3, linestyle='--')
ax.scatter(x, y, s=400, facecolor='lightseagreen', edgecolor='k', zorder=3)

ax.text(23, 0.95, 'π', fontsize=30, color='k', fontweight='bold')

ax.set_xlabel('Voltage (V)', fontsize=30, color='k', fontweight='bold')
ax.set_ylabel('Phase (rad/π)', fontsize=30, color='k', fontweight='bold')
ax.tick_params(axis='both', labelsize=27, colors='k')
ax.set_xlim([0,35])
ax.set_ylim([0,2.0])

fig2.tight_layout()
plt.grid(True)
fig2.savefig('plot/Phase_plot.png')