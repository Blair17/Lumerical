import os
import numpy as np
import matplotlib.pyplot as plt
import glob
from scipy.interpolate import LinearNDInterpolator
from matplotlib.pyplot import cm

def last_9chars(x):
    return(x[-8:])

root = os.getcwd()

# files_refl = glob.glob('/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Au_Al2O3_ITO/Al2O3_Layer_Inv/test/data/refl/*.txt')
# sorted_refl = sorted(files_refl, key = last_9chars)  

# files_phase = glob.glob('/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Au_Al2O3_ITO/Al2O3_Layer_Inv/test/data/phase/*.txt')
# sorted_phase = sorted(files_phase, key = last_9chars)  

# l_array = []
# p_array = []

file_refl = '/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Au_Al2O3_ITO/Al2O3_Layer_Inv/test/data/refl/reflection0.00.txt'
file_phase = '/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Au_Al2O3_ITO/Al2O3_Layer_Inv/test/data/phase/phase0.00.txt'


datafilename = file_refl
datafilepath = os.path.join(
    root,
    datafilename)
l = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=1,
    unpack=True)
    
datafilename = file_phase
datafilepath = os.path.join(
    root,
    datafilename)
p = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=1,
    unpack=True)

x = np.linspace(500, 1500, 1000)
y = np.linspace(0, 0.1, 11)

rnge = np.arange(0, 11, 1)

opt_buffer_values = np.linspace(0, 100, 11)
x_tick_loc = ['']
x_ticks = [ '600', '500', '1000', '1500']

# s1 = np.array([q / np.pi for q in p_array])
# s = np.array([k - min(k) for k in s1])

# r = np.array([q * 100 for q in l_array])

# r_test = r[::2]
# s_test = s[::2]
# opt_test = opt_buffer_values[::2]
# rnge = np.arange(0, 11, 1)

fig, ax = plt.subplots(1, 2, figsize=[10,5])
color1 = iter(cm.jet(np.linspace(0, 1, len(rnge))))

ax[0].plot(l)
ax[0].legend(frameon=True, loc='lower left', ncol=2, fontsize=11)
ax[0].set_xlabel('Wavelength [nm]', fontsize=18, fontweight='bold')
ax[0].set_ylabel('Reflection [%]', fontsize=18, fontweight='bold')
# ax[0].set_ylim(0, 100)
ax[0].tick_params(axis='both', labelsize=18)
# ax[0].set_xticklabels(x_ticks)

ax[1].plot(p)
ax[1].legend(frameon=True, loc='lower left', ncol=2, fontsize=11)
ax[1].set_xlabel('Wavelength [nm]', fontsize=18, fontweight='bold')
ax[1].set_ylabel('Phase [rad/π]', fontsize=18, fontweight='bold')
# ax[1].set_ylim(0, 1.05)
ax[1].tick_params(axis='both', labelsize=18)
ax[1].set_xticklabels(x_ticks) 

plt.tight_layout()
plt.savefig('Plasmonic_Al2O3_Variation_Indv_plot.png')
plt.show()