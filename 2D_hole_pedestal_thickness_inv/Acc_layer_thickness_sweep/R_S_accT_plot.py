import numpy as np
import os
import matplotlib.pyplot as plt
import glob

def last_9chars(x):
    return(x[-10:])

def array_to_list_of_strings(lst):
    return [str(np.round(x,2)) for x in lst]

def linear_func(x, m, c):
    return m * x + c

root = os.getcwd()

files_refl = glob.glob('/Volumes/Sam/Lumerical/2D_GMR/acc_thickness_sweep/high_res_high_simtime/data/refl/*.txt')
sorted_refl = sorted(files_refl, key = last_9chars)  

files_phase = glob.glob('/Volumes/Sam/Lumerical/2D_GMR/acc_thickness_sweep/high_res_high_simtime/data/phase/*.txt')
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
 
datafilename = '/Volumes/Sam/Lumerical/2D_GMR/acc_thickness_sweep/higher_res/data/wav/wavelength.txt'
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

n_array = []
pd_array = []

labels = np.linspace(1,10,10)
labels = array_to_list_of_strings(labels)

colors = len(r_array)
cmap = plt.cm.rainbow(np.linspace(0,1,colors))

fig, ax = plt.subplots(figsize=([10,5]))
for index, (l, p, i, k) in enumerate(zip(r_hundred, p_min, labels, range(colors))):
    ax.plot(wav, l, label=i, color=cmap[k], lw=2)
    ax.set_xlabel('Wavelength (nm)', fontsize=18, color='k', fontweight='bold')
    ax.set_ylabel('Transmission', fontsize=18, color='k', fontweight='bold')
    ax.set_xlim([740,770])
    ax.set_ylim([0.1,100])
    ax.legend(loc='lower left', frameon=True, fontsize=14, ncols=2, framealpha=0, labelcolor='k')
    ax.tick_params(axis='both', labelsize=16, colors='k')
    ax.set_title('Accumulation Layer Thickness vs Transmission', fontsize=20)
    

plt.tight_layout()
plt.savefig('2D_hole_pedestal_thickness_inv/Acc_layer_thickness_sweep/R_S_accT_Thickness.png', dpi=300)