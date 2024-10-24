import os
import numpy as np
import matplotlib.pyplot as plt
import glob

root = os.getcwd()

def last_9chars(x):
    return(x[-7:])

root = os.getcwd()
# files = glob.glob('/Volumes/Sam/Lumerical/Optimising_GMRM/Pedestal_Investigation/Index_Shifts/10nm_Layer/variation/*.txt')
# sorted_array = sorted(files, key = last_9chars)  
# print(sorted_array)

# l_array = []
# r_array = []

# for file in sorted_array:
#     datafilename = file
#     datafilepath = os.path.join(
#         root,
#         datafilename)
#     l, r = np.genfromtxt(
#         fname=datafilepath,
#         delimiter=",",
#         skip_header=3,
#         unpack=True)
    # l_array.append(l)
    # r_array.append(r)  

datafilename = '/Volumes/Sam/Lumerical/2D_GMR/acc_layer_mid/nacc1.0_R.txt'
datafilepath = os.path.join(
    root,
    datafilename)
lamR1, refl1 = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=3,
    unpack=True)

# datafilename = '/Volumes/Sam/Lumerical/Optimising_GMRM/Pedestal_Investigation/Index_Shifts/10nm_Layer/variation/n_S22_2.00.txt'
# datafilepath = os.path.join(
#     root,
#     datafilename)
# lamP1, phase1 = np.genfromtxt(
#     fname=datafilepath,
#     delimiter=",",
#     skip_header=3,
#     unpack=True)

datafilename = '/Volumes/Sam/Lumerical/2D_GMR/acc_layer_mid/nacc2.0_R.txt'
datafilepath = os.path.join(
    root,
    datafilename)
lamR2, refl2 = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=3,
    unpack=True)

# datafilename = '/Volumes/Sam/Lumerical/Optimising_GMRM/Pedestal_Investigation/Index_Shifts/10nm_Layer/variation/n_R_2.20.txt'
# datafilepath = os.path.join(
#     root,
#     datafilename)
# lamP2, phase2 = np.genfromtxt(
#     fname=datafilepath,
#     delimiter=",",
#     skip_header=3,
#     unpack=True)

datafilename = '/Volumes/Sam/Lumerical/2D_GMR/acc_layer_mid/nacc3.0_R.txt'
datafilepath = os.path.join(
    root,
    datafilename)
lamR3, refl3 = np.genfromtxt(
    fname=datafilepath,
    delimiter=",",
    skip_header=3,
    unpack=True)

# datafilename = '/Volumes/Sam/Lumerical/Optimising_GMRM/Pedestal_Investigation/Index_Shifts/10nm_Layer/variation/n_R_2.20.txt'
# datafilepath = os.path.join(
#     root,
#     datafilename)
# lamP3, phase3 = np.genfromtxt(
#     fname=datafilepath,
#     delimiter=",",
#     skip_header=3,
#     unpack=True)

# datafilename = '/Volumes/Sam/Lumerical/Optimising_GMRM/Pedestal_Investigation/Index_Shifts/10nm_Layer/variation/n_R_2.20.txt'
# datafilepath = os.path.join(
#     root,
#     datafilename)
# lamR4, refl4 = np.genfromtxt(
#     fname=datafilepath,
#     delimiter=",",
#     skip_header=3,
#     unpack=True)

# datafilename = '/Volumes/Sam/Lumerical/Optimising_GMRM/Pedestal_Investigation/Index_Shifts/10nm_Layer/variation/n_R_2.20.txt'
# datafilepath = os.path.join(
#     root,
#     datafilename)
# lamP4, phase4 = np.genfromtxt(
#     fname=datafilepath,
#     delimiter=",",
#     skip_header=3,
#     unpack=True)

# phaseAu_rad = phase1 / np.pi
# phaseAu2 = phaseAu_rad - min(phaseAu_rad)

# phaseCr_rad = phase2 / np.pi
# phaseCr2 = phaseCr_rad - min(phaseCr_rad)

# phase_rad = phase3 / np.pi
# phase3a = phase_rad - min(phase_rad)

# phase_rad4 = phase4 / np.pi
# phase4a = phase_rad4 - min(phase_rad4)

fig, axs = plt.subplots(figsize=[10,7])
axs.plot(lamR1, refl1, lw=3, color='k', label='n = 1.0')
axs.plot(lamR2, refl2, lw=3, color='crimson', label='n = 2.0')
axs.plot(lamR3, refl3, lw=3, color='darkviolet', label='n = 3.0')
# axs.plot(lamR4, refl4, lw=3, color='c', label='n = 2.00')

# ax2 = axs.twinx()
# ax2.plot(lamP4, phase4a, lw=3, color='c', label='Phase n = 2.00', linestyle='--')
# ax2.plot(lamP1, phaseAu2, lw=3, color='crimson', label='Phase', linestyle='-')
# ax2.plot(lamP3, phase3a, lw=3, color='darkviolet', label='Phase n = 2.10', linestyle='--')
# ax2.plot(lamP2, phaseCr2, lw=3, color='crimson', label='No Charge Layer Phase', linestyle='--')

# axs.set_ylim([-0.01, 1.01])
axs.set_xlabel('Wavelength [nm]', fontsize=22, fontweight='bold')
axs.set_ylabel('Transmission', fontsize=22, fontweight='bold', color='k')
# ax2.set_ylabel('Phase [π rad]', fontsize=22, fontweight='bold', rotation=270, labelpad=30, color='crimson')
axs.legend(frameon=True, loc='center left', prop={'size': 12})
# ax2.legend(frameon=True, loc='center right', prop={'size': 12})
# ax2.set_ylim([-0.05, 2.05])
plt.xlim([740, 770])
# plt.axvline(x=789, color='k', lw=1)
axs.tick_params(axis='both', labelsize=20)
# ax2.tick_params(axis='both', labelsize=20)

# res = 800.79 - 805.16
# print(res)

# plt.title('GMRM Structure w 5 nm AlOx Adhesion Layer \n ', fontsize=22, fontweight='bold')
plt.tight_layout()
plt.savefig('nacc.png')
# plt.show()