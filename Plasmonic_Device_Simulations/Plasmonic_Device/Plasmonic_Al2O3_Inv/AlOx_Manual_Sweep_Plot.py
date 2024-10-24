import os
import numpy as np
import matplotlib.pyplot as plt
import glob
from scipy.interpolate import LinearNDInterpolator
from matplotlib.pyplot import cm

def last_9chars(x):
    return(x[-6:])

root = os.getcwd()

files_refl = glob.glob('/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Au_Al2O3_ITO/Al2O3_Layer_Inv/Manual_buffer_Sweeps/refl/*.txt')
sorted_refl = sorted(files_refl, key = last_9chars)  

files_phase = glob.glob('/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Au_Al2O3_ITO/Al2O3_Layer_Inv/Manual_buffer_Sweeps/phase/*.txt')
sorted_phase = sorted(files_phase, key = last_9chars)  

l_array = []
p_array = []

for file in sorted_refl:
    datafilename = file
    datafilepath = os.path.join(
        root,
        datafilename)
    wl, l = np.genfromtxt(
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
    wp, p = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=1,
        unpack=True)
    p_array.append(p) 

l_array = np.array(l_array)
p_array = np.array(p_array)
        
x = np.linspace(500, 1500, 1000)
rnge = np.arange(0, 6, 1)

opt_buffer_values = [0, 10, 20, 30, 40, 50]
x_ticks = [ '600', '500', '1000', '1500']

s1 = np.array([q / np.pi for q in p_array])
s = np.array([k - min(k) for k in s1])

r = np.array([q * 100 for q in l_array])

fig, ax = plt.subplots(1, 1, figsize=[10,7])
fig1, ax1 = plt.subplots(figsize=[10,7])
color1 = iter(cm.jet(np.linspace(0, 1, len(rnge))))

for i, k in zip(rnge, color1):
    ax.plot(wl, r[i], c=k, lw=5, label = f'{opt_buffer_values[i]} nm')
    ax.legend(frameon=True, loc='lower left', ncol=2, fontsize=25)
    ax.set_xlabel('Wavelength (nm)', fontsize=25, fontweight='bold')
    ax.set_ylabel('Reflection (%)', fontsize=25, fontweight='bold')
    ax.set_ylim(0, 100)
    ax.set_xlim(551, 849)
    ax.tick_params(axis='both', labelsize=25)
    # ax[0].set_xticklabels(x_ticks)
    fig.tight_layout()
    fig.savefig('Plasmonic_Manual_Al2O3_sweep_R.png', dpi=300)

    ax1.plot(wl, s[i], c=k, lw=5, label = f'{opt_buffer_values[i]} nm')
    ax1.legend(frameon=True, loc='lower left', ncol=2, fontsize=25)
    ax1.set_xlabel('Wavelength (nm)', fontsize=25, fontweight='bold')
    ax1.set_ylabel('Phase (rad/π)', fontsize=25, fontweight='bold')
    ax1.set_ylim(0, 3)
    ax1.set_xlim(551, 849)
    ax1.tick_params(axis='both', labelsize=25)
    # ax[1].set_xticklabels(x_ticks)
    fig1.tight_layout()
    fig1.savefig('Plasmonic_Manual_Al2O3_sweep_P.png', dpi=300)

# plt.savefig('Plasmonic_Manual_Al2O3_sweep.png', dpi=300)
# plt.show()