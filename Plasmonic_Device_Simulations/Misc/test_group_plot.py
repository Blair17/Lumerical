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

def last_9chars(x):
    return(x[-17:])

root = os.getcwd()

files_refl = glob.glob('/Volumes/Sam/GMR1/2024/240124/R1/*.txt')
sorted_refl = sorted(files_refl, key = last_9chars) 

datafilename = '/Volumes/Sam/Lumerical/Plasmonic_GMRM/Index_Changes/GMRM_optimised_R.txt'
datafilepath = os.path.join(
        root,
        datafilename)
wav_sim, r_sim = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=3,
        unpack=True)
    
r_array = []
wav_array = []

for file in sorted_refl:
    datafilename = file
    datafilepath = os.path.join(
        root,
        datafilename)
    wav, l = np.genfromtxt(
        fname=datafilepath,
        delimiter=";",
        skip_header=1,
        unpack=True)
    r_array.append(l)

r_hundred = []
for r in r_array:
    r1 = r * 100
    r_hundred.append(r1)
    
labels = ['-15 V', '-10 V', '-5 V', '-1 V', '0 V', '1 V', '5 V', '10 V', '15 V', 'Simulation']

colors = len(r_array)
cmap = plt.cm.rainbow(np.linspace(0,1,colors))   

x_tick_locs = [725, 735, 745, 755]
x_ticks = [780, 790, 800, 810]

wav_array = np.linspace(498.7,1001, 3647)

r_sim = (r_sim*100)[::-1]
r_hundred.append(r_sim)

fig, ax = plt.subplots(figsize=([10,7]))
ax.plot(wav_sim-50, r_sim, lw=7, color='k', label='Simulation')

for index, (l, k, lab) in enumerate(zip(r_hundred, range(colors), labels)):
    ax.plot(wav-3, l-19, color=cmap[::-1][k], label=lab, lw=7)
    ax.set_xlabel('Wavelength (nm)', fontsize=30, color='k', fontweight='bold')
    ax.set_ylabel('Reflection (%)', fontsize=30, color='k', fontweight='bold')
    ax.tick_params(axis='both', labelsize=27, colors='k')
    ax.set_xticks(x_tick_locs)
    ax.set_xticklabels(x_ticks)
    
    plt.xlim([725, 760])
    # plt.xlim([700, 800])
    plt.ylim([0.01,100])

ax.legend(frameon=True, fontsize=21, loc='lower left', ncols=2)

plt.tight_layout()
plt.savefig('test.png')
# plt.show()