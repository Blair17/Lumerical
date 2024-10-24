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

def last_9chars(x):
    return(x[-12:])

def find_closest_value(array, target_value):
    index = np.abs(array - target_value).argmin()
    closest_value = array[index]
    return index, closest_value

def reverse_lists(input_lists):
    reversed_lists = [lst[::-1] for lst in input_lists]
    return reversed_lists

def array_to_string(input):
    n = range(0,len(input))
    return [str(input[i]) for i in n]

def sigmoid(x, L, x0, k, b):
    return L / (1 + np.exp(-k * (x - x0))) + b

def sigmoid_fit(x, y):
    initial_guess = [1, np.median(x), 1, 0]
    params, covariance = curve_fit(sigmoid, x, y, p0=initial_guess)

    x_fit = np.linspace(min(x), max(x), 1000)
    y_fit = sigmoid(x_fit, *params)

    return x_fit, y_fit

root = os.getcwd()

files_refl = glob.glob('/Volumes/Sam/Lumerical/Final_modulator/modulation_data/160724_02/data/refl/*.txt')
sorted_refl = sorted(files_refl, key = last_9chars)  

files_phase = glob.glob('/Volumes/Sam/Lumerical/Final_modulator/modulation_data/160724_02/data/phase/*.txt')
sorted_phase = sorted(files_phase, key = last_9chars)  

r_array = []
p_array = []

for file in sorted_refl:
    datafilename = file
    datafilepath = os.path.join(
        root,
        datafilename)
    l = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=1,
        unpack=True)
    r_array.append(l)
    
for file in sorted_phase:
    datafilename = file
    datafilepath = os.path.join(
        root,
        datafilename)
    p = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=1,
        unpack=True)
    p_array.append(p)
    
datafilename = '/Volumes/Sam/Lumerical/Final_modulator/modulation_data/160724_02/data/wav/wavelength.txt'
datafilepath = os.path.join(
        root,
        datafilename)
wav = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=0,
        unpack=True)

p_min = []
for p in p_array:
    p1 = (p - min(p)) / np.pi
    p_min.append(p1)

r_hundred = []
for r in r_array:
    r1 = r * 100
    r_hundred.append(r1)

index, closest_value = find_closest_value(wav, 842)

reflect_array = []
phase_array = []

nacc_array = [1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00]

for i in range(len(r_hundred)):
    k = r_hundred[i][index]
    ink = p_min[i][index]
    reflect_array.append(k)
    phase_array.append(ink)

clr = 'black'
colors = len(r_array)
cmap = plt.cm.rainbow(np.linspace(0,1,colors))

fig, ax = plt.subplots(figsize=([10,7]))
fig1, ax1 = plt.subplots(figsize=([10,7]))

for index, (l, p, k) in enumerate(zip(r_hundred, p_min, range(colors))):
    ax.plot(wav, l, color=cmap[k], lw=4)
    ax.set_xlabel('Wavelength (nm)', fontsize=27, color='k', fontweight='bold')
    ax.set_ylabel('Reflection (%)', fontsize=27, color='k', fontweight='bold')
    # ax[0].axvline(x=564, ymin=0, ymax=1, color='w', lw=1, linestyle='--')
    ax.set_xlim([838,850])
    # ax.set_ylim([0,100])
    # ax[0].legend(loc='center right', frameon=True, fontsize=18, labelcolor='k')
    ax.tick_params(axis='both', labelsize=25, colors='k')
    # ax.set_xticks(x_tick_locs)
    # ax.set_xticklabels(x_ticks)
    # ax.axvline(x=744, ymin=0, ymax=1, color='k', lw=1, linestyle='--')
    # ax[0].set_facecolor(clr)
    # ax[0].spines[align].set_color('w')
    # ax[0].text(-0.92, 0.97, f'Max Refl shift = {diff1.round(2)} %', fontsize=12, color='w', 
            #    fontweight='bold', transform=ax[1].transAxes, ha='center', va='center')
    
    ax1.plot(wav, p, color=cmap[k], lw=4)
    ax1.set_xlabel('Wavelength (nm)', fontsize=27, color='k', fontweight='bold')
    ax1.set_ylabel('Phase (rad/π)', fontsize=27, color='k', fontweight='bold')
    # ax[1].axvline(x=564, ymin=0, ymax=1, color='w', lw=1, linestyle='--')
    ax1.set_xlim([838,850])
    # ax1.set_ylim([0,2.2])
    # ax[1].legend(loc='center right', frameon=True, fontsize=18, labelcolor='k')
    ax1.tick_params(axis='both', labelsize=25, colors='k')
    # ax1.set_yticks(y_tick_loc)
    # ax1.set_xticks(x_tick_locs)
    # ax1.set_xticklabels(x_ticks)
    # ax1.axvline(x=744, ymin=0, ymax=1, color='k', lw=1, linestyle='--')
    # ax[1].set_facecolor(clr)
    # ax[1].spines[align].set_color('w')
    # ax[1].text(0.68, 0.97, f'Phase shift = {diff.round(2)} rad/π', fontsize=12, color='w', fontweight='bold', transform=ax[1].transAxes, ha='center', va='center')
    
y_tick_locies = [0, 2, 4]
labs = ['-10 V', '0 V', '10 V']
norm = plt.Normalize(0, 4)
scalar_mappable = cm.ScalarMappable(cmap='rainbow', norm=norm)
scalar_mappable.set_array([])  # You need to set an array for the scalar mappable

cbar = fig.colorbar(scalar_mappable, ax=ax, orientation='vertical', location='right')
# cbar.set_label('Accumulation layer index (RIU)', fontsize=23, color='k', fontweight='bold', rotation=270, labelpad=30)
cbar.ax.tick_params(labelsize=25, colors='k')
cbar.ax.set_yticks(y_tick_locies)
cbar.ax.set_yticklabels(labs, fontweight='bold')

fig.tight_layout()
fig.savefig('plot/Refl_highres.png', dpi=300)

cbar1 = fig1.colorbar(scalar_mappable, ax=ax1, orientation='vertical', location='right')
# cbar.set_label('Accumulation layer index (RIU)', fontsize=23, color='k', fontweight='bold', rotation=270, labelpad=30)
cbar1.ax.tick_params(labelsize=25, colors='k')
cbar1.ax.set_yticks(y_tick_locies)
cbar1.ax.set_yticklabels(labs, fontweight='bold')

fig1.tight_layout()
fig1.savefig('plot/Phase_highres.png', dpi=300)

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

x = 1.93
y = 1

# colors = ["white", "turquoise", "lightseagreen", "teal", "darkslategrey"]

x_ticks = ['-22', '-11', '0', '11', '22']

x_fit, y_fit = sigmoid_fit(nacc_array, diff_array)

fig2, ax = plt.subplots(figsize=[10,7])
ax.plot(voltage_array, diff_array, lw=3, color='darkslategrey')
ax.plot(x_fit[::-1], y_fit, lw=5, color='teal')

# ax.axhline(y=1, xmin=0, xmax=0.49, color='turquoise', lw=3, linestyle='--')
# ax.axvline(x=x, ymin=0, ymax=0.52, color='turquoise', lw=3, linestyle='--')
# ax.scatter(x, y, s=400, facecolor='lightseagreen', edgecolor='k', zorder=3)
# ax.text(x + 0.1, 0.95, 'π', fontsize=30, color='k', fontweight='bold')

ax.set_xlabel('Voltage (V)', fontsize=30, color='k', fontweight='bold')
# ax.set_xlabel('Index (RIU)', fontsize=30, color='k', fontweight='bold')
ax.set_ylabel('Phase (rad/π)', fontsize=30, color='k', fontweight='bold')
ax.tick_params(axis='both', labelsize=27, colors='k')
ax.set_xticklabels(x_ticks)
ax.set_xlim([1,3])
ax.set_ylim([0.00001,2.0])

fig2.tight_layout()
plt.grid(True)
fig2.savefig('plot/Phase_plot.png')