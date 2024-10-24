import os
import numpy as np
import matplotlib.pyplot as plt
import glob
import pandas as pd
from matplotlib import cm
# from matplotlib.cm import ScalarMappable
# from matplotlib.colors import ListedColormap
# from scipy.interpolate import UnivariateSpline
import statsmodels.api as sm
from scipy.optimize import curve_fit
import scienceplots

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

plt.style.use("dark_background")
plt.style.use(['science', 'nature', 'pink'])

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
cmap = cmap[::-1]

xticks = [793, 795, 797, 799, 801, 803, 805, 807]
y_ticks = [20, 40, 60, 80, 100]
    
pparam = dict(xlabel='Wavelength (nm)', ylabel=r'Reflection ($\%$)')

fig, ax = plt.subplots()
for index, (l, k) in enumerate(zip(r_hundred, range(colors))):
    ax.plot(wav, l, color=cmap[k], lw=2)
    # ax.plot(wav, l, lw=2)
ax.autoscale(tight=True)
ax.set(**pparam)
ax.set_xticklabels(xticks)
ax.set_yticks(y_ticks)

y_tick_locies = [0, 2, 4]
labs = ['-2 V', '0 V', '2 V']
norm = plt.Normalize(0, 4)
scalar_mappable = cm.ScalarMappable(cmap='rainbow', norm=norm)
scalar_mappable.set_array([])

cbar = fig.colorbar(scalar_mappable, ax=ax, orientation='vertical', location='right')
cbar.ax.tick_params(labelsize=8, colors='w')
cbar.ax.set_yticks(y_tick_locies)
cbar.ax.set_yticklabels(labs, fontweight='bold')

plt.xlim([836,850])
plt.ylim([0,100])
fig.savefig('plot/Refl_test.png', dpi=600)
plt.close()

pparam1 = dict(xlabel='Wavelength (nm)', ylabel=r'Phase (rad/$\pi$)')

fig1, ax1 = plt.subplots()
for index, (p, k) in enumerate(zip(p_min, range(colors))):
    ax1.plot(wav, p, color=cmap[k], lw=2)
    # ax1.plot(wav, p, lw=2)
ax1.autoscale(tight=True)
ax1.set(**pparam1)
ax1.set_xticklabels(xticks)

cbar1 = fig1.colorbar(scalar_mappable, ax=ax1, orientation='vertical', location='right')
cbar1.ax.tick_params(labelsize=8, colors='w')
cbar1.ax.set_yticks(y_tick_locies)
cbar1.ax.set_yticklabels(labs, fontweight='bold')

plt.xlim([836,850])
plt.ylim([-0.1,2.0])
fig1.savefig('plot/phase_test.png', dpi=600)
plt.close()

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

x_ticks = [1.00, 1.50, 2.0, 2.50, 3.00]
x_tick_labs = ['-2', '-1', '0', '1', '2']

x_fit, y_fit = sigmoid_fit(nacc_array, diff_array)

pparam2 = dict(xlabel='Voltage (V)', ylabel=r'$\Delta$Phase (rad/$\pi$)')

df = pd.DataFrame({
    'x': x_fit,
    'y': y_fit,
})
df.to_csv('Phase_data.csv', index=False)

fig2, ax2 = plt.subplots()
# ax.plot(voltage_array, diff_array, lw=3, color='darkslategrey')
# ax2.plot(x_fit[::-1], y_fit, lw=2, color=cmap[-1])
ax2.plot(x_fit[::-1], y_fit, lw=2)
ax2.set(**pparam2)

# ax.axhline(y=1, xmin=0, xmax=0.49, color='turquoise', lw=3, linestyle='--')
# ax.axvline(x=x, ymin=0, ymax=0.52, color='turquoise', lw=3, linestyle='--')
# ax.scatter(x, y, s=400, facecolor='lightseagreen', edgecolor='k', zorder=3)
# ax.text(x + 0.1, 0.95, 'π', fontsize=30, color='k', fontweight='bold')

ax2.set_xticks(x_ticks)
ax2.set_xticklabels(x_tick_labs)
ax2.set_xlim([1,3])
ax2.set_ylim([0.00001,2.0])

# fig2.tight_layout()
# plt.grid(True)
fig2.savefig('plot/Phase_plot.png', dpi=600)