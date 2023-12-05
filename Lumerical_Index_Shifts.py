import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import numpy as np
import os 
import scipy as scipy
import scipy.ndimage
import sys
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits import axes_grid1
np.set_printoptions(threshold=sys.maxsize)

def add_colorbar(im, aspect=20, pad_fraction=0.5, **kwargs):
    """Add a vertical color bar to an image plot."""
    divider = axes_grid1.make_axes_locatable(im.axes)
    width = axes_grid1.axes_size.AxesY(im.axes, aspect=1./aspect)
    pad = axes_grid1.axes_size.Fraction(pad_fraction, width)
    current_ax = plt.gca()
    cax = divider.append_axes("right", size=width, pad=pad)
    plt.sca(current_ax)
    return im.axes.figure.colorbar(im, cax=cax, **kwargs)

root = os.getcwd()

datafilename = '/Volumes/Sam/Lumerical/Optimising_GMRM/Pedestal_Investigation/Index_Shifts/10nm_Layer/789.6nm/Index_Sweep_2.00_2.20_5steps_P429_FF0.86_GT150_PT150_OB_339_R.txt'
datafilepath = os.path.join(
    root,
    datafilename)
refl = np.genfromtxt(
    fname=datafilepath,
    delimiter=" ",
    skip_header=1,
    unpack=True)

datafilename = '/Volumes/Sam/Lumerical/Optimising_GMRM/Pedestal_Investigation/Index_Shifts/10nm_Layer/789.6nm/Index_Sweep_2.00_2.20_5steps_P429_FF0.86_GT150_PT150_OB_339_S22.txt'
datafilepath = os.path.join(
    root,
    datafilename)
phase = np.genfromtxt(
    fname=datafilepath,
    delimiter=" ",
    skip_header=1,
    unpack=True)

# FFs =      ['1.95', '1.97', '1.98', '2.00', '2.01', '2.03', '2.04', '2.06', '2.08', '2.09', 
#             '2.11', '2.12', '2.14', '2.16', '2.17', '2.19', '2.20', '2.22', '2.23', '2.25']
# FFs =      ['1.95', '1.98', '2.01', '2.04', '2.08', '2.11', '2.14', '2.17', '2.20', '2.23']
FFs =      ['2.00', '2.05', '2.10', '2.15', '2.20']
# x_ticks =  ['780', '790', '800', '810', '820']
x_ticks =  ['770', '770', '785', '800', '820']
x_tick_loc = [0, 150, 300, 450, 600]

variance = 5

d = []
totalshift = []
diff = []
for y in range(0,variance,1):
    c = np.unwrap(phase[y, :], period=np.pi)
    totalshift.append(c[-1]-c[0])
    a = np.diff(c)
    diff.append(np.append(a, 0))
    d.append(c)
s1 = np.array([(q+np.pi) / np.pi for q in d])
s = np.array([k - min(k) for k in s1])

flipped_refl = np.fliplr(refl)
flipped_s = np.fliplr(s)

k = np.arange(0,variance,1)

new_r = flipped_refl[::2]
new_s = flipped_s[::2]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[10,7])
for index, p in enumerate(k):
    ax1.plot(flipped_refl[p, :], label=[x for x in FFs][index], lw=2) 
    ax1.legend(frameon=True, loc='lower left', ncol=1, fontsize=16)
    ax1.set_xlabel('Wavelength [nm]', fontsize=24, fontweight='bold')
    ax1.set_ylabel('Reflection', fontsize=24, fontweight='bold')
    ax1.set_ylim(-0.01, 1.0)
    ax1.tick_params(axis='both', labelsize=21)
    ax1.set_xticks(x_tick_loc)
    ax1.set_xticklabels(x_ticks)
    ax1.set_xlim(150, 475)

for index, p in enumerate(k):
    ax2.plot(flipped_s[p, :], label=[x for x in FFs][index], lw=2)
    ax2.legend(frameon=True, loc='lower left', ncol=1, fontsize=16)
    ax2.set_xlabel('Wavelength [nm]', fontsize=24, fontweight='bold')
    ax2.set_ylabel('Phase [π rad]', fontsize=24, fontweight='bold')
    ax2.tick_params(axis='both', labelsize=21)
    ax2.set_ylim(-0.01, 2.0)
    ax2.set_xticks(x_tick_loc)
    ax2.set_xticklabels(x_ticks)
    ax2.set_xlim(150, 475)
    
ax1.axvline(x=315, color='k', lw=2, ls='--')
ax2.axvline(x=297, color='k', lw=2, ls='--')
# plt.suptitle('AlOx - 10 nm Active Charge Layer', fontsize=16, fontweight='bold')

# fig, ax = plt.subplots()
# ax.plot(phase[1])
# ax.plot(phase[2])
# # ax.plot(phase[2])
# # ax.plot(phase[3])
# # ax.plot(phase[4])

# print(phase[1])

plt.tight_layout()
plt.savefig('/Users/samblair/Desktop/figy.png', dpi=300)
# plt.show()