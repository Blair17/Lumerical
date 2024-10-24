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

datafilename = '/Volumes/Sam/Lumerical/Optimising_GMRM/Pedestal_Investigation/Optical_Buffer_Variations/NEW_TE_OptBuffer_T_Variation_0.1-1.5um_0.8FF_2.1n_421P_PEDESTAL150_R.txt'
datafilepath = os.path.join(
    root,
    datafilename)
refl = np.genfromtxt(
    fname=datafilepath,
    delimiter=" ",
    skip_header=1,
    unpack=True)

datafilename = '/Volumes/Sam/Lumerical/Optimising_GMRM/Pedestal_Investigation/Optical_Buffer_Variations/NEW_TE_OptBuffer_T_Variation_0.1-1.5um_0.8FF_2.1n_421P_PEDESTAL150_S22.txt'
datafilepath = os.path.join(
    root,
    datafilename)
phase = np.genfromtxt(
    fname=datafilepath,
    delimiter=" ",
    skip_header=1,
    unpack=True)

opt_buffer_values = np.linspace(0.1, 1.1, num=200)

y_labels = ['0.1', '0.3', '0.5', '0.7', '0.9', '1.1']
# x_labels = ['620','630', '640', '650', '660', '670', '680']
x_labels = ['780', '785', '790', '800', '805', '810', '815', '820']
x_new_labels = ['700', '780', '786', '793', '800', '806', '813', '820']
# x_new_labels = ['680', '620', '635', '650', '665', '680']

rnge = np.arange(0, 200, 1)
high_refl = []
phase_vals = []
for r in rnge:
        if min(refl[r]) > 0.9188:
            high_refl.append(r)
            # phase_vals.append(high_refl[r])
            
color1 = iter(cm.jet(np.linspace(0, 1, len(high_refl))))

d = []
# totalshift = []
# diff = []

for y in range(0,200,1):
    c = np.unwrap(phase[y, :], period=np.pi)
    # totalshift.append(c[-1]-c[0])
    # a = np.diff(c)
    # diff.append(np.append(a, 0))
    d.append(c)
s1 = np.array([q / np.pi for q in d])
s = np.array([k - min(k) for k in s1])

# s1 = np.array([q / np.pi for q in phase])
# s = np.array([k - min(k) for k in s1])
# s = phase

flipped_refl = np.fliplr(refl)
flipped_s = np.fliplr(s)

fig, axs = plt.subplots(2, 2, figsize=[11,7])
mycmap1 = plt.get_cmap('turbo')
mycmap2 = plt.get_cmap('plasma')

q = axs[0, 0].imshow(flipped_refl, 
              cmap=mycmap1,
              aspect='auto', 
              extent=[0, 70, 0, 100], # wavelength(400,1), bufferT(1, 200)
              interpolation='bicubic', 
              origin='lower')
axs[0,0].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
axs[0,0].set_ylabel('Optical Buffer \n Layer Thickness [um]', fontsize=17, fontweight='bold')
axs[0,0].tick_params(axis='both', labelsize=13)
axs[0,0].set_yticklabels(y_labels)
axs[0,0].set_xticklabels(x_labels)
axs[0,0].axhline(37, color='w', lw=1, linestyle='--')
cbar = add_colorbar(q)
cbar.ax.set_title('Refl', fontsize=16, fontweight='bold')
cbar.ax.tick_params(labelsize=15)

# x_ticks = ['605', '620', '635', '650', '665', '680']
color1 = iter(cm.jet(np.linspace(0, 1, len(high_refl))))

for i, k in zip(high_refl, color1):
    x_ticks = ['780', '786', '793', '800', '806', '820']
    axs[0, 1].plot(flipped_refl[i], label=f'{opt_buffer_values[i].round(3)} um', c=k)
    # ax.plot(refl[150, :],lw=3, label='0')
    axs[0,1].legend(frameon=True, loc='lower left', ncol=2, fontsize=11)
    axs[0,1].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
    axs[0,1].set_ylabel('Reflection', fontsize=16, fontweight='bold')
    axs[0,1].set_ylim(0, 1.0)
    axs[0,1].tick_params(axis='both', labelsize=14)
    axs[0,1].set_xticklabels(x_new_labels)

k = axs[1, 0].imshow(flipped_s, 
              cmap=mycmap2,
              aspect='auto', 
              extent=[0, 70, 0, 100],
              interpolation='bicubic', 
              origin='lower')
axs[1,0].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
axs[1,0].set_ylabel('Optical Buffer \n Layer Thickness [um]', fontsize=16, fontweight='bold')
axs[1,0].tick_params(axis='both', labelsize=13)
cbar = add_colorbar(k)
cbar.ax.set_title('Phase', fontsize=16, fontweight='bold')
cbar.ax.tick_params(labelsize=16)
axs[1,0].set_yticklabels(y_labels)
axs[1,0].set_xticklabels(x_labels)
axs[1,0].axhline(37, color='w', lw=1, linestyle='--')

# for i in range(flipped_s):
#    c = next(color)
#    plt.plot(x, y, c=c)

color2 = iter(cm.jet(np.linspace(0, 1, len(high_refl))))
for i, k in zip(high_refl, color2):
    # c = next(color)
    x_ticks = ['780', '786', '793', '800', '806', '820']
    axs[1, 1].plot(flipped_s[i], label=f'{opt_buffer_values[i].round(3)} um', c=k)
    # ax.plot(refl[150, :],lw=3, label='0')
    axs[1,1].legend(frameon=True, loc='upper right', ncol=2, fontsize=11)
    axs[1,1].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
    axs[1,1].set_ylabel('Phase [π rad]', fontsize=16, fontweight='bold')
    axs[1,1].tick_params(axis='both', labelsize=14)
    axs[1,1].set_xticklabels(x_new_labels)

plt.tight_layout()
plt.savefig('/Users/samblair/Desktop/Code/Projects/Lumerical/Optical_Buffer_Variations.png', dpi=300)
# plt.show()