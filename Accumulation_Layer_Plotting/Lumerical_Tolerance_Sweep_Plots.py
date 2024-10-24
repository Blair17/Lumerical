import matplotlib.pyplot as plt
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

datafilename = '/Volumes/Sam/Lumerical/Optimising_GMRM/Pedestal_Investigation/Index_Shifts/10nm_Layer/Index_Sweep_1.95_2.23_20steps_P440_FF0.86_GT150_PT150_OB_339_R.txt'
datafilepath = os.path.join(
    root,
    datafilename)
refl = np.genfromtxt(
    fname=datafilepath,
    delimiter=" ",
    skip_header=1,
    unpack=True)

datafilename = '/Volumes/Sam/Lumerical/Optimising_GMRM/Pedestal_Investigation/Index_Shifts/10nm_Layer/Index_Sweep_1.95_2.23_20steps_P440_FF0.86_GT150_PT150_OB_339_S22.txt'
datafilepath = os.path.join(
    root,
    datafilename)
phase = np.genfromtxt(
    fname=datafilepath,
    delimiter=" ",
    skip_header=1,
    unpack=True)

# y_labels = ['0.5', '0.6', '0.7', '0.8', '0.9', '1.0']
# y_labels = ['1.90', '1.95', '2.00', '2.05', '2.10', '2.15 ', '2.20']
y_labels = ['1.95', '2.00', '2.05', '2.10', '2.15', '2.20 ', '2.25']
# y_labels = ['50', '125', '200', '275', '350', '425 ', '500']
# x_labels = ['0.620','0.630', '0.640', '0.650', '0.660', '0.670', '0.680']
# x_labels = ['700', '740', '780', '820', '860', '900']
x_labels = ['780','785', '790', '795', '800', '805', '810', '815', '820']

variance = 20

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

# FFs = ['0.5', '0.54', '0.59', '0.64',
#        '0.68', '0.73', '0.77', '0.82',
#        '0.86', '0.91', '0.95', '1.0']           # FF

# FFs = ['50', '100', '150', '200', '250', 
#        '300', '350', '400', '450', '500']         # GT

# FFs = ['1.90', '1.94', '1.99', '2.03', 
#        '2.07', '2.11', '2.16', '2.20']

FFs = ['1.95', '1.97', '1.98', '2.00', '2.01', '2.03', '2.04', '2.06', '2.08', '2.09', 
       '2.11', '2.12', '2.14', '2.16', '2.17', '2.19', '2.20', '2.22', '2.23', '2.25']

fig, axs = plt.subplots(2, 2, figsize=[10,7])
mycmap1 = plt.get_cmap('turbo')

q = axs[0, 0].imshow(np.fliplr(refl), 
              cmap=mycmap1,
              aspect='auto', 
              extent=[0, 80, 0, 60],
              interpolation='bicubic', 
              origin='lower')
axs[0,0].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
axs[0,0].set_ylabel('n', fontsize=16, fontweight='bold')
axs[0,0].tick_params(axis='both', labelsize=10)
cbar = add_colorbar(q)
cbar.ax.set_title('Refl', fontsize=16, fontweight='bold')
cbar.ax.tick_params(labelsize=10)
axs[0,0].set_yticklabels(y_labels)
axs[0,0].set_xticklabels(x_labels)

x_ticks = ['605', '780', '790', '800', '820']
for index, p in enumerate(range(0,variance,1)):
    axs[0, 1].plot(refl[p, :], label=[x for x in FFs][index])
# ax.plot(refl[150, :],lw=3, label='0')
    axs[0,1].legend(frameon=True, loc='lower left', ncol=4, fontsize=9)
    axs[0,1].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
    axs[0,1].set_ylabel('Reflection', fontsize=16, fontweight='bold')
    axs[0,1].set_ylim(0, 1.0)
    axs[0,1].tick_params(axis='both', labelsize=14)
    axs[0,1].set_xticklabels(x_ticks)

k = axs[1, 0].imshow(np.fliplr(s), 
              cmap='plasma',
              aspect='auto', 
              extent=[0, 80, 0, 60],
              interpolation='bicubic', 
              origin='lower')
axs[1,0].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
axs[1,0].set_ylabel('n', fontsize=16, fontweight='bold')
axs[1,0].tick_params(axis='both', labelsize=10)
cbar = add_colorbar(k)
cbar.ax.set_title('Phase', fontsize=16, fontweight='bold')
cbar.ax.tick_params(labelsize=10)
axs[1,0].set_yticklabels(y_labels)
axs[1,0].set_xticklabels(x_labels)

x_ticks = ['605', '780', '790', '800', '820']
for index, p in enumerate(range(0,variance,1)):
    axs[1, 1].plot(s[p, :], label=[x for x in FFs][index])
# ax.plot(refl[150, :],lw=3, label='0')
    axs[1,1].legend(frameon=True, loc='upper left', ncol=4, fontsize=9)
    axs[1,1].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
    axs[1,1].set_ylabel('Phase [π rad]', fontsize=16, fontweight='bold')
    axs[1,1].tick_params(axis='both', labelsize=14)
    axs[1,1].set_ylim(0, 2.1)
    axs[1,1].set_xticklabels(x_ticks)

plt.tight_layout()
plt.show()