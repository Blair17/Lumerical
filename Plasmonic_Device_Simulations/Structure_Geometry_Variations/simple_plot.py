import os
import numpy as np
import matplotlib.pyplot as plt
import glob
from matplotlib.pyplot import cm

def last_9chars(x):
    return(x[-9:])

root = os.getcwd()

datafilename = '/Volumes/Sam/Lumerical/Plasmonics/160424_Full_Device_Scripts_Data/thickness_variation/data/refl/reflection30.txt'
datafilepath = os.path.join(
        root,
        datafilename)
r = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=1,
        unpack=True)

datafilename = '/Volumes/Sam/Lumerical/Plasmonics/160424_Full_Device_Scripts_Data/thickness_variation/data/phase/phase30.txt'
datafilepath = os.path.join(
        root,
        datafilename)
p = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=1,
        unpack=True)

datafilename = '/Volumes/Sam/Lumerical/Plasmonics/160424_Full_Device_Scripts_Data/thickness_variation/data/wav/wavelength.txt'
datafilepath = os.path.join(
        root,
        datafilename)
wav = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=0,
        unpack=True)

# s1 = np.array([q / np.pi for q in p])
# s = np.array([k - min(k) for k in s1])

r = np.array([q * 100 for q in r])

fig, ax = plt.subplots(1, 1, figsize=[10,7])
fig1, ax1 = plt.subplots(figsize=[10,7])


ax.plot(wav, r, lw=5)
ax.legend(frameon=True, loc='lower right', ncol=1, fontsize=20)
ax.set_xlabel('Wavelength (nm)', fontsize=28, fontweight='bold')
ax.set_ylabel('Reflection (%)', fontsize=28, fontweight='bold')
# ax.set_ylim(0, 100)
# ax.set_xlim(701, 1199)
ax.tick_params(axis='both', labelsize=27)
# ax[0].set_xticklabels(x_ticks)
fig.tight_layout()
fig.savefig('t_R.png', dpi=300)

ax1.plot(wav, p, lw=5)
ax1.legend(frameon=True, loc='upper left', ncol=1, fontsize=20)
ax1.set_xlabel('Wavelength (nm)', fontsize=28, fontweight='bold')
ax1.set_ylabel('Phase (rad/π)', fontsize=28, fontweight='bold')
# ax1.set_ylim(0, 2.3)
# ax1.set_xlim(701, 1199)
ax1.tick_params(axis='both', labelsize=27)
# ax[1].set_xticklabels(x_ticks)
fig1.tight_layout()
fig1.savefig('t_P.png', dpi=300)