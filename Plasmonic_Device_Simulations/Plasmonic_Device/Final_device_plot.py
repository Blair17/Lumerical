import numpy as np
import matplotlib.pyplot as plt
import os

root = os.getcwd()

datafilename = '/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Au_Al2O3_ITO/Al2O3_Layer_Inv/nacc_sweeps/optimised/Reflection.txt'
datafilepath = os.path.join(
        root,
        datafilename)
wav0, refl = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=1,
        unpack=True)

datafilename = '/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Au_Al2O3_ITO/Al2O3_Layer_Inv/nacc_sweeps/optimised/Phase.txt'
datafilepath = os.path.join(
        root,
        datafilename)
wav1, phase = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=1,
        unpack=True)

r_hundred = []
for r in refl:
    r1 = r * 100
    r_hundred.append(r1)
    
p_min = []
for p in phase:
    p1 = (p - min(phase)) / np.pi
    p_min.append(p1)

fig, ax = plt.subplots(figsize=[10,7])
ax.plot(wav0, r_hundred, lw=6, c='midnightblue', linestyle='-', label='Reflection')
ax1 = ax.twinx()
ax1.plot(wav1, p_min, lw=6, c='mediumspringgreen', linestyle='-', label='Phase')
ax.set_xlabel('Wavelength (nm)', fontsize=27, color='k', fontweight='bold')
ax1.set_ylabel('Phase (rad/π)', fontsize=27, color='k', fontweight='bold')
ax.set_ylabel('Reflection (%)', fontsize=27, color='k', fontweight='bold')
ax.tick_params(axis='both', labelsize=25, colors='k')
ax1.tick_params(axis='both', labelsize=25, colors='k')
ax1.set_ylim([0.01, 2.3])
ax.set_xlim([600,1000])
# ax.legend(loc=0, frameon=True, fontsize=25, facecolor='w', framealpha=1)
fig.legend(loc="lower left", bbox_to_anchor=(0, 0), bbox_transform=ax.transAxes, fontsize=25, facecolor='w', framealpha=1)
plt.tight_layout()
plt.savefig('finaldevice.png', dpi=300)