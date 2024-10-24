import os
import numpy as np
import matplotlib.pyplot as plt
import glob

def last_9chars(x):
    return(x[-8:])

def find_closest_value(array, target_value):
    index = np.abs(array - target_value).argmin()
    closest_value = array[index]
    return index, closest_value

root = os.getcwd()

files_refl = glob.glob('/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Updated_good_structure_scripts/Cu_adhesion_top_bottom/index_sweep/data/refl/*.txt')
sorted_refl = sorted(files_refl, key = last_9chars)  

files_phase = glob.glob('/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Updated_good_structure_scripts/Cu_adhesion_top_bottom/index_sweep/data/phase/*.txt')
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
 
datafilename = '/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Updated_good_structure_scripts/Cu_adhesion_top_bottom/index_sweep/data/wav/wavelength.txt'
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
    
waveOI = 784

index, closest_value = find_closest_value(wav, waveOI)

n_array = []
pd_array = []

for r, p, i in zip(p_min, r_hundred, range(len(r_hundred))):
    ink = p_min[i][index]
    k = r_hundred[i][index]
    n_array.append(ink)
    pd_array.append(k)

diff = np.abs(n_array[0] - n_array[4])
# print(diff)

diff1 = np.abs(pd_array[0] - pd_array[4])

labels = ['1.00', '1.50', '2.00', '2.50', '3.00']
align = ['left', 'right', 'top', 'bottom']

# clr = 'black'
colors = len(r_array)
cmap = plt.cm.rainbow(np.linspace(0,1,colors))
cmap = cmap

fig, ax = plt.subplots(1, 2, figsize=([10,5]))
for index, (l, p, i, k) in enumerate(zip(r_hundred, p_min, labels, range(colors))):
    ax[0].plot(wav, l, label=i, color=cmap[k], lw=7)
    ax[0].set_xlabel('Wavelength (nm)', fontsize=18, fontweight='bold')
    ax[0].set_ylabel('Reflection', fontsize=18, fontweight='bold')
    ax[0].axvline(x=waveOI, ymin=0, ymax=1, lw=1, linestyle='--')
    ax[0].set_xlim([650,900])
    # ax[0].set_ylim([-1,100])
    # ax[0].set_ylim([-1,100])
    ax[0].legend(loc='lower right', frameon=True, fontsize=14, framealpha=0)
    ax[0].tick_params(axis='both', labelsize=14)
    ax[0].text(-0.92, 0.97, f'Max refl shift = {diff1.round(2)} %', fontsize=12, 
               fontweight='bold', transform=ax[1].transAxes, ha='center', va='center')
    
    ax[1].plot(wav, p, label=i, color=cmap[k], lw=7)
    ax[1].set_xlabel('Wavelength (nm)', fontsize=18, fontweight='bold')
    ax[1].set_ylabel('Phase (rad/π)', fontsize=18, fontweight='bold')
    ax[1].axvline(x=waveOI, ymin=0, ymax=1, lw=1, linestyle='--')
    ax[1].set_xlim([650,900])
    ax[1].set_ylim([-0.1,2.2])
    ax[1].legend(loc='lower left', frameon=True, fontsize=14, framealpha=0)
    ax[1].tick_params(axis='both', labelsize=14)
    ax[1].text(0.68, 0.97, f'Phase shift = {diff.round(2)} rad/π', fontsize=12, fontweight='bold', transform=ax[1].transAxes, ha='center', va='center')

plt.tight_layout()
plt.savefig('Double_Cu_adhesion_Phase_shift.png', dpi=300)
# plt.show()