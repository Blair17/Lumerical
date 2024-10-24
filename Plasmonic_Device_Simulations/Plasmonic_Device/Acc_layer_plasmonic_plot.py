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

root = os.getcwd()

files_refl = glob.glob('/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Au_Al2O3_ITO/Al2O3_Layer_Inv/nacc_sweeps/high_res_sweep/data/refl/*.txt')
sorted_refl = sorted(files_refl, key = last_9chars)  

files_phase = glob.glob('/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Au_Al2O3_ITO/Al2O3_Layer_Inv/nacc_sweeps/high_res_sweep/data/phase/*.txt')
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

p_min = []
for p in p_array:
    p1 = (p - min(p)) / np.pi
    p_min.append(p1)

r_hundred = []
for r in r_array:
    r1 = r * 100
    r_hundred.append(r1)

wav = np.linspace(500,1000,1000)
index, closest_value = find_closest_value(wav, 760)

reflect_array = []
phase_array = []

reverse_r = reverse_lists(r_hundred)  
reverse_p = reverse_lists(p_min)   
# nacc_array = np.linspace(1.0,3.0,5) 

nacc_array = [2.00, 1.67, 1.40, 1.06, 0.85]
nacc_rounded = np.round(nacc_array,20)
# print(nacc_rounded)
nacc_strings = array_to_string(nacc_rounded)
# print(nacc_strings)

for i in range(len(r_hundred)):
    k = reverse_r[i][index]
    ink = reverse_p[i][index]
    reflect_array.append(k)
    phase_array.append(ink)
    
print(phase_array)
    
# df = pd.DataFrame({'nacc': nacc_array, 'reflection': reflect_array, 'phase': phase_array})
# df.to_csv('/Users/samblair/Desktop/0nm_Buffer.csv', index=False)

# labels = ['1.0', '1.5', '2.0', '2.5', '3.0']
labels =  ['2.00', '1.67', '1.40', '1.06', '0.85']
labels =  ['0 V', '10 V', '20 V', '30 V', '35 V']
align = ['left', 'right', 'top', 'bottom']

clr = 'black'
colors = len(r_array)
cmap = plt.cm.rainbow(np.linspace(0,1,colors))
# cmap = cmap[::-1]
# print(colors)
y_tick_loc=[0, 0.5, 1.0, 1.5, 2.0]

x_tick_locs = [700, 720, 740, 760, 780]
x_ticks = [740, 760, 780, 800, 820]

fig, ax = plt.subplots(figsize=([10,7]))
fig1, ax1 = plt.subplots(figsize=([10,7]))

for index, (l, p, k) in enumerate(zip(r_hundred, p_min, range(colors))):
    ax.plot(wav, l, color=cmap[k], lw=8)
    ax.set_xlabel('Wavelength (nm)', fontsize=27, color='k', fontweight='bold')
    ax.set_ylabel('Reflection (%)', fontsize=27, color='k', fontweight='bold')
    # ax[0].axvline(x=564, ymin=0, ymax=1, color='w', lw=1, linestyle='--')
    ax.set_xlim([690,790])
    ax.set_ylim([0,100])
    # ax[0].legend(loc='center right', frameon=True, fontsize=18, labelcolor='k')
    ax.tick_params(axis='both', labelsize=25, colors='k')
    ax.set_xticks(x_tick_locs)
    ax.set_xticklabels(x_ticks)
    # ax.axvline(x=744, ymin=0, ymax=1, color='k', lw=1, linestyle='--')
    # ax[0].set_facecolor(clr)
    # ax[0].spines[align].set_color('w')
    # ax[0].text(-0.92, 0.97, f'Max Refl shift = {diff1.round(2)} %', fontsize=12, color='w', 
            #    fontweight='bold', transform=ax[1].transAxes, ha='center', va='center')
    
    ax1.plot(wav, p, color=cmap[k], lw=8)
    ax1.set_xlabel('Wavelength (nm)', fontsize=27, color='k', fontweight='bold')
    ax1.set_ylabel('Phase (rad/π)', fontsize=27, color='k', fontweight='bold')
    # ax[1].axvline(x=564, ymin=0, ymax=1, color='w', lw=1, linestyle='--')
    ax1.set_xlim([690,790])
    ax1.set_ylim([0,2.2])
    # ax[1].legend(loc='center right', frameon=True, fontsize=18, labelcolor='k')
    ax1.tick_params(axis='both', labelsize=25, colors='k')
    ax1.set_yticks(y_tick_loc)
    ax1.set_xticks(x_tick_locs)
    ax1.set_xticklabels(x_ticks)
    # ax1.axvline(x=744, ymin=0, ymax=1, color='k', lw=1, linestyle='--')
    # ax[1].set_facecolor(clr)
    # ax[1].spines[align].set_color('w')
    # ax[1].text(0.68, 0.97, f'Phase shift = {diff.round(2)} rad/π', fontsize=12, color='w', fontweight='bold', transform=ax[1].transAxes, ha='center', va='center')

y_tick_locies = [0, 2, 4]
labs = ['0 V', '15 V', '30 V']
norm = plt.Normalize(0, 4)
scalar_mappable = cm.ScalarMappable(cmap='rainbow', norm=norm)
scalar_mappable.set_array([])  # You need to set an array for the scalar mappable

cbar = fig.colorbar(scalar_mappable, ax=ax, orientation='vertical', location='right')
# cbar.set_label('Accumulation layer index (RIU)', fontsize=23, color='k', fontweight='bold', rotation=270, labelpad=30)
cbar.ax.tick_params(labelsize=25, colors='k')
cbar.ax.set_yticks(y_tick_locies)
cbar.ax.set_yticklabels(labs, fontweight='bold')

fig.tight_layout()
fig.savefig('Refl_highres.png', dpi=300)

cbar1 = fig1.colorbar(scalar_mappable, ax=ax1, orientation='vertical', location='right')
# cbar.set_label('Accumulation layer index (RIU)', fontsize=23, color='k', fontweight='bold', rotation=270, labelpad=30)
cbar1.ax.tick_params(labelsize=25, colors='k')
cbar1.ax.set_yticks(y_tick_locies)
cbar1.ax.set_yticklabels(labs, fontweight='bold')

fig1.tight_layout()
fig1.savefig('Phase_highres.png', dpi=300)

# voltage_array = [0, 10, 20, 30, 35]
voltage_array = np.linspace(0,35,30)

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
x = [14.2]

y1 = [1.5]
x1 = [25]

y_tick_locations = [0, 0.5, 1.0, 1.5]

fig2, ax = plt.subplots(figsize=[10,7])
ax.plot(voltage_array, diff_array, lw=8, color='mediumspringgreen')

ax.axhline(y=1, xmin=0, xmax=0.45, color='k', lw=3, linestyle='--')
ax.axvline(x=x, ymin=0.26, ymax=0.6, color='k', lw=3, linestyle='--')
ax.axvline(x=x, ymin=0, ymax=0.15, color='k', lw=3, linestyle='--')
ax.scatter(x, y, s=400, facecolor='crimson', edgecolor='k', zorder=3)

ax.axhline(y=1.5, xmin=0, xmax=0.75, color='k', lw=3, linestyle='--')
ax.axvline(x=x1, ymin=0.72, ymax=0.9, color='k', lw=3, linestyle='--')
ax.axvline(x=x1, ymin=0, ymax=0.57, color='k', lw=3, linestyle='--')
ax.scatter(x1, y1, s=400, facecolor='crimson', edgecolor='k', zorder=3)

ax.text(13.5, 0.25, 'π', fontsize=30, color='k', fontweight='bold')
ax.text(23.8, 1.0, r'$\bf{\frac{3}{2}π}$', fontsize=30, color='k', fontweight='bold')

ax.set_xlabel('Voltage (V)', fontsize=30, color='k', fontweight='bold')
# ax.set_ylabel('Reflection (%)', fontsize=18, color='k', fontweight='bold')
ax.set_ylabel('Phase (rad/π)', fontsize=30, color='k', fontweight='bold')
ax.tick_params(axis='both', labelsize=27, colors='k')
ax.set_xlim([0,33])
# ax.set_ylim([0,2.2])
ax.set_yticks(y_tick_locations)
# ax1.tick_params(axis='both', labelsize=14, colors='k')

fig2.tight_layout()
plt.grid(True)
fig2.savefig('0nm_nacc_test.png')
print(reflect_array)

fig4, ax4 = plt.subplots()
ax4.plot(voltage_array, reflect_array, lw=8, color='mediumspringgreen')
fig4.savefig('0nm_refl_test.png')
# plt.show()