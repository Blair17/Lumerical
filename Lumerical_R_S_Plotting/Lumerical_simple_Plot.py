import os
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
plt.style.use(['science', 'nature', 'custom'])

root = os.getcwd()

datafilename = '/Volumes/Sam/Lumerical/TiO2_Inv/R_60ITO_TM_n1.8.txt'
datafilepath = os.path.join(
    root,
    datafilename)
lamR1, refl1 = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=1,
    unpack=True)

# datafilename = '/Volumes/Sam/Lumerical/Thorpe_paper_simulations/test_structure/Double_ITO/R_n3.0.txt'
# datafilepath = os.path.join(
#     root,
#     datafilename)
# lamR2, refl2 = np.genfromtxt(
#     fname=datafilepath,
#     delimiter=",",
#     skip_header=3,
#     unpack=True)

# datafilename = '/Volumes/Sam/Lumerical/Plasmonics/Gold_nanoballs/S.txt'
# datafilepath = os.path.join(
#     root,
#     datafilename)
# wavp, phase = np.genfromtxt(
#     fname=datafilepath,
#     delimiter=",",
#     skip_header=1,
#     unpack=True)

# phase_rad = phase / np.pi
# phase2 = phase_rad - min(phase_rad)

refl = refl1 * 100
# lamR1 = lamR1 * 1
# refl2 = refl2 * 100

yticklocs = [0.5, 1.0, 1.5, 2.0]
labels = [0.5, 1.0, 1.5, 2.0]

pparam = dict(xlabel='Wavelength (nm)', ylabel=r'Reflection (\%)')

fig, ax = plt.subplots()
ax.plot(lamR1, refl)
# ax.legend(loc=0, fontsize=6)
ax.autoscale(tight=True)
ax.set(**pparam)
ax.set_ylim([0,100])
fig.savefig('R_n1.8.png', dpi=600)
plt.close()

# fig, axs = plt.subplots(figsize=[10,7])
# axs.plot(lamR1, refl, lw=4, color='navy', label=r'n$_{acc}$ = 2.0')
# axs.plot(lamR2, refl2, lw=4, color='mediumspringgreen', label=r'n$_{acc}$ = 3.0')
# # axs.plot(lamR1[::-1], refl2, lw=6, color='k', label='nacc = 1.0')

# # ax2 = axs.twinx()
# # ax2.plot(lamR1, phase2, lw=4, color='mediumspringgreen', label='Phase', linestyle='-')

# axs.set_xlabel('Wavelength [nm]', fontsize=28)
# axs.set_ylabel('Reflection [%]', fontsize=28, color='k')
# # ax2.set_ylabel('Phase [π rad]', fontsize=22, rotation=270, labelpad=30, color='k')
# axs.legend(frameon=True, loc='center left', prop={'size': 20})
# # ax2.legend(frameon=True, loc='center right', prop={'size': 18})
# # # ax2.set_ylim([0.0, 2.5])
# axs.set_ylim([0.1, 105])
# axs.set_xlim([800, 880])
# ax2.set_yticks(yticklocs)
# ax2.set_yticklabels(labels)
# plt.xlim([400, 900])

maxn2 = np.round( lamR1[np.argmax(refl)], 3)
print(maxn2)
# maxn3 = np.round( lamR2[np.argmax(refl2)], 3)
# diff = np.round( np.abs((maxn3 - maxn2)), 2)  

# axs.tick_params(axis='both', labelsize=25)

# plt.text(0.8, 0.5, f'Δλ = {diff} nm', 
#          horizontalalignment='center', 
#          verticalalignment='center', 
#          transform=axs.transAxes, 
#          fontsize=25,
#          color='k')

# plt.tight_layout()
# plt.savefig('R.png')
# plt.show()