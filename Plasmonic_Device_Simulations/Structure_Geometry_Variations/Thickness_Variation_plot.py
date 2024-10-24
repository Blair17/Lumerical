import os
import numpy as np
import matplotlib.pyplot as plt
import glob
from matplotlib.pyplot import cm

def last_9chars(x):
    return(x[-9:])

root = os.getcwd()

files_refl = glob.glob('/Volumes/Sam/Lumerical/Plasmonics/160424_Full_Device_Scripts_Data/width_variation/data/refl/*.txt')
sorted_refl = sorted(files_refl, key = last_9chars)  

files_phase = glob.glob('/Volumes/Sam/Lumerical/Plasmonics/160424_Full_Device_Scripts_Data/width_variation/data/phase/*.txt')
sorted_phase = sorted(files_phase, key = last_9chars)  

l_array = []
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
    l_array.append(l) 

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
    
datafilename = '/Volumes/Sam/Lumerical/Plasmonics/160424_Full_Device_Scripts_Data/width_variation/data/wav/wavelength.txt'
datafilepath = os.path.join(
        root,
        datafilename)
wav = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=0,
        unpack=True)

l_array = np.array(l_array)
p_array = np.array(p_array)

x = np.linspace(600, 2000, 1000)
rnge = np.arange(0, 11, 1)

# opt_buffer_values = [0, 10, 20, 30, 40, 50]
opt_buffer_values = np.linspace(30,100,11)

s1 = np.array([q / np.pi for q in p_array])
s = np.array([k - min(k) for k in s1])

r = np.array([q * 100 for q in l_array])

# sliced_OBT_array = np.array(np.squeeze([opt_buffer_values[0:55:5]]))
# sliced_r = np.array(np.squeeze([r[0:55:5]]))
# sliced_s = np.array(np.squeeze([s[0:55:5]]))

fig, ax = plt.subplots(1, 1, figsize=[10,7])
fig1, ax1 = plt.subplots(figsize=[10,7])
color1 = iter(cm.jet(np.linspace(0, 1, len(rnge))))

for i, k in zip(rnge, color1):
    ax.plot(wav, r[i], c=k, lw=4, label = f'{opt_buffer_values[i]} nm')
    ax.legend(frameon=True, loc='lower right', ncol=1, fontsize=20)
    ax.set_xlabel('Wavelength (nm)', fontsize=28, fontweight='bold')
    ax.set_ylabel('Reflection (%)', fontsize=28, fontweight='bold')
    ax.set_ylim(0, 100)
    ax.set_xlim(601, 1199)
    ax.tick_params(axis='both', labelsize=27)
    # ax[0].set_xticklabels(x_ticks)
    fig.tight_layout()
    fig.savefig('Width_variation_R.png', dpi=300)

    ax1.plot(wav, s[i], c=k, lw=4, label = f'{opt_buffer_values[i]} nm')
    ax1.legend(frameon=True, loc='upper right', ncol=1, fontsize=20)
    ax1.set_xlabel('Wavelength (nm)', fontsize=28, fontweight='bold')
    ax1.set_ylabel('Phase (rad/π)', fontsize=28, fontweight='bold')
    ax1.set_ylim(0, 2.5)
    ax1.set_xlim(601, 1199)
    ax1.tick_params(axis='both', labelsize=27)
    # ax[1].set_xticklabels(x_ticks)
    fig1.tight_layout()
    fig1.savefig('Width_variation_P.png', dpi=300)