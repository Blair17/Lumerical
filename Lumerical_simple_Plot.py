import os
import numpy as np
import matplotlib.pyplot as plt

root = os.getcwd()

datafilename = '/Volumes/Sam/Lumerical/635_Optimised_Device/635_resonance_R.txt'
datafilepath = os.path.join(
    root,
    datafilename)
lamR1, refl1 = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=3,
    unpack=True)

datafilename = '/Volumes/Sam/Lumerical/635_Optimised_Device/635_resonance_S.txt'
datafilepath = os.path.join(
    root,
    datafilename)
lamphi, phase = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=3,
    unpack=True)

phase_rad = phase / np.pi
phase2 = phase_rad - min(phase_rad)

fig, axs = plt.subplots(figsize=[10,7])
axs.plot(lamR1, refl1, lw=3, color='k', label='Refl')

ax2 = axs.twinx()
ax2.plot(lamR1, phase2, lw=3, color='crimson', label='Phase', linestyle='-')

axs.set_ylim([-0.01, 1.01])
axs.set_xlabel('Wavelength [nm]', fontsize=22, fontweight='bold')
axs.set_ylabel('Reflection', fontsize=22, fontweight='bold', color='k')
ax2.set_ylabel('Phase [π rad]', fontsize=22, fontweight='bold', rotation=270, labelpad=30, color='crimson')
axs.legend(frameon=True, loc='center left', prop={'size': 12})
ax2.legend(frameon=True, loc='center right', prop={'size': 12})
# ax2.set_ylim([-0.05, 2.05])
# plt.xlim([780, 820])
# plt.axvline(x=789, color='k', lw=1)
axs.tick_params(axis='both', labelsize=20)
ax2.tick_params(axis='both', labelsize=20)

# res = 800.79 - 805.16
# print(res)

plt.tight_layout()
plt.savefig('635_resonance.png')