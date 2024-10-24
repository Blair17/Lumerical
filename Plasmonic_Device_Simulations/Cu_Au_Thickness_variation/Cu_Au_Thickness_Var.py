import os
import numpy as np
import matplotlib.pyplot as plt
import glob

def last_9chars(x):
    return(x[-9:])

def find_closest_value(array, target_value):
    index = np.abs(array - target_value).argmin()
    closest_value = array[index]
    return index, closest_value

root = os.getcwd()

files_refl = glob.glob('/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Updated_good_structure_scripts/Cu_Adhesion_Au_Antenna_plasmonic_device/120424_Cu_thickness_sweep/data/refl/*.txt')
sorted_refl = sorted(files_refl, key = last_9chars) 

files_phase = glob.glob('/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Updated_good_structure_scripts/Cu_Adhesion_Au_Antenna_plasmonic_device/120424_Cu_thickness_sweep/data/phase/*.txt')
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

datafilename = '/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Updated_good_structure_scripts/Cu_Adhesion_Au_Antenna_plasmonic_device/120424_Cu_thickness_sweep/data/wav/wavelength.txt'
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
    
print(len(r_hundred[0]))
    
# wav = np.linspace(500, 1000, 2001)

# index, closest_value = find_closest_value(wav, 635)

# n_array = []
# pd_array = []

# for r, p, i in zip(p_min, r_hundred, range(len(r_hundred))):
#     ink = p_min[i][index]
#     k = r_hundred[i][index]
#     n_array.append(ink)
#     pd_array.append(k)

# diff = np.abs(n_array[0] - n_array[2])
# print(diff)

# diff1 = np.abs(pd_array[0] - pd_array[1])

labels = ['0 nm', '2.50 nm', '5.0 nm', '7.5 nm', '10.0 nm']
align = ['left', 'right', 'top', 'bottom']

# clr = 'black'
colors = len(r_array)
cmap = plt.cm.rainbow(np.linspace(0,1,colors))

fig, ax = plt.subplots(1, 2, figsize=([10,5]))
for index, (l, p, i, k) in enumerate(zip(r_hundred, p_min, labels, range(colors))):
    ax[0].plot(wav, l, label=i, color=cmap[k], lw=7)
    ax[0].set_xlabel('Wavelength (nm)', fontsize=18, color='k', fontweight='bold')
    ax[0].set_ylabel('Reflection', fontsize=18, color='k', fontweight='bold')
    # ax[0].axvline(x=798, ymin=0, ymax=1, color='k', lw=1, linestyle='--')
    ax[0].set_xlim([600,1000])
    # ax[0].set_ylim([0,100])
    ax[0].legend(loc='lower left', frameon=True, fontsize=10, framealpha=0, labelcolor='k')
    ax[0].tick_params(axis='both', labelsize=18, colors='k')
    # ax[0].set_facecolor(clr)
    # ax[0].spines[align].set_color('w')
    # ax[0].text(-0.92, 0.97, f'Max Refl shift = {diff1.round(2)} %', fontsize=12, color='w', 
    #            fontweight='bold', transform=ax[1].transAxes, ha='center', va='center')
    
    ax[1].plot(wav, p, label=i, color=cmap[k], lw=7)
    ax[1].set_xlabel('Wavelength (nm)', fontsize=18, color='k', fontweight='bold')
    ax[1].set_ylabel('Phase (rad/π)', fontsize=18, color='k', fontweight='bold')
    # ax[1].axvline(x=635, ymin=0, ymax=1, color='k', lw=1, linestyle='--')
    ax[1].set_xlim([600,1000])
    # ax[1].set_ylim([0.0,2.1])
    ax[1].legend(loc='center left', frameon=True, fontsize=10, framealpha=0, labelcolor='k')
    ax[1].tick_params(axis='both', labelsize=18, colors='k')
    # ax[1].set_facecolor(clr)
    # ax[1].spines[align].set_color('w')
    # ax[1].text(0.68, 0.97, f'Phase shift = {diff.round(2)} rad/π', fontsize=12, color='w', fontweight='bold', transform=ax[1].transAxes, ha='center', va='center')

plt.tight_layout()
plt.savefig('Cu_Au_Inv_2.png', dpi=300)