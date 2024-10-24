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

datafilename = '/Volumes/Sam/Lumerical/635_Optimised_Device/field_plots/635nm.txt'
datafilepath = os.path.join(
    root,
    datafilename)
field1 = np.genfromtxt(
    fname=datafilepath,
    delimiter=" ",
    skip_header=1,
    unpack=True)

datafilename = '/Volumes/Sam/Lumerical/635_Optimised_Device/field_plots/contours.txt'
datafilepath = os.path.join(
    root,
    datafilename)
field_r = np.genfromtxt(
    fname=datafilepath,
    delimiter=" ",
    skip_header=1,
    unpack=True)

x_tick_loc = [0, 125, 250, 375, 500] # x = 51

yticks = ['-400', '-200', '-100', '0', '100', '200', '300', '400']

xticks = ['-205', '-102', '0', '102', '205']

# fig, (ax1, ax2, ax3) = plt.subplots(1 , 3, figsize=[14,7])
fig, ax1 = plt.subplots(figsize=[10,7])
mycmap1 = plt.get_cmap('gnuplot2')

k = ax1.imshow((field1), 
              cmap=mycmap1,
              aspect='auto', 
              extent=[0, 500, 0, 600],
              interpolation='bicubic',
              origin='lower')
ax1.contour(field_r, levels=0, extent=[0, 500, 0, 600], colors='w', linewidths=3)
ax1.set_xlabel('X [nm]', fontsize=24, fontweight='bold')
ax1.set_ylabel('Z [nm]', fontsize=24, fontweight='bold')
ax1.tick_params(axis='both', labelsize=18)
cbar = add_colorbar(k)
cbar.ax.set_title('Ex', fontsize=22, fontweight='bold')
cbar.ax.tick_params(labelsize=22)
ax1.set_xticks(x_tick_loc)

# ax1.axhline(y=300, color='w', lw=2, linestyle='-')

# ax1.axhline(y=450, xmin=0, xmax=0.36, color='w', lw=2, linestyle='-')
# ax1.axhline(y=450, xmin=0.64, xmax=1, color='w', lw=2, linestyle='-')

# ax1.axvline(x=181.75, ymin=0.5, ymax=0.75, color='w', lw=2, linestyle='-')
# ax1.axvline(x=318.5, ymin=0.5, ymax=0.75, color='w', lw=2, linestyle='-')

ax1.set_yticklabels(yticks)
ax1.set_xticklabels(xticks)

plt.text(50, 540, 'Air',  color='white', fontweight='bold', fontsize=25, ha='center', va='center')
plt.text(50, 220, 'ITO',  color='white', fontweight='bold', fontsize=25, ha='center', va='center')
# plt.text(30, 250, r'$\bf{{Al_{2}}{O_{3}}}$',  color='white', fontweight='bold', fontsize=20, ha='center', va='center')
plt.text(50, 60, r'$\bf{Si{O_{2}}}$',  color='white', fontweight='bold', fontsize=25, ha='center', va='center')
# plt.ylim([100,550])
# plt.ylim([1,699])

# val1 = len(field1[12]) * 3/4
# array2 = np.sum(field1[:round(val1)])

# val2 = len(field1[13]) * 0.6
# array3 = np.sum(field1[:round(val2)])

# tot = array2 + array3
# print(tot.round(2))

print(sum(field1[13]))

# ax1.set_title('n = 2.0', fontsize=16, fontweight='bold')

# r = ax2.imshow(np.fliplr(field2), 
#               cmap=mycmap1,
#               aspect='auto', 
#               extent=[0, 500, 0, 600],
#               interpolation='bicubic', 
#               origin='lower')
# ax2.set_xlabel('X [nm]', fontsize=16, fontweight='bold')
# ax2.set_ylabel('Z [nm]', fontsize=16, fontweight='bold')
# ax2.tick_params(axis='both', labelsize=14)
# cbar = add_colorbar(r)
# cbar.ax.set_title('Ey', fontsize=16, fontweight='bold')
# cbar.ax.tick_params(labelsize=14)
# ax2.set_xticks(x_tick_loc)
# ax2.axhline(y=145, color='w', lw=2, linestyle='-')
# ax2.axhline(y=150, color='w', lw=1, linestyle='--')
# # ax2.axhline(y=155, color='w', lw=1, linestyle='--')
# ax2.axhline(y=300, xmin=0.0, xmax=0.14, color='w', lw=2, linestyle='-')
# ax2.axhline(y=300, xmin=0.86, xmax=1.0, color='w', lw=2, linestyle='-')
# ax2.axhline(y=450, xmin=0.14, xmax=0.86, color='w', lw=2, linestyle='-')
# ax2.axvline(x=70, ymin=0.5, ymax=0.75, color='w', lw=2, linestyle='-')
# ax2.axvline(x=430, ymin=0.5, ymax=0.75, color='w', lw=2, linestyle='-')
# ax2.set_yticklabels(yticks)
# ax2.set_xticklabels(xticks)

# ax2.set_title('n = 2.1', fontsize=16, fontweight='bold')

# w = ax3.imshow(np.fliplr(field2), 
#               cmap=mycmap1,
#               aspect='auto', 
#               extent=[0, 500, 0, 600],
#               interpolation='bicubic', 
#               origin='lower')
# ax3.set_xlabel('X [nm]', fontsize=16, fontweight='bold')
# ax3.set_ylabel('Z [nm]', fontsize=16, fontweight='bold')
# ax3.tick_params(axis='both', labelsize=14)
# cbar = add_colorbar(w)
# cbar.ax.set_title('Ey', fontsize=16, fontweight='bold')
# cbar.ax.tick_params(labelsize=14)
# ax3.set_xticks(x_tick_loc)
# ax3.axhline(y=145, color='w', lw=2, linestyle='-')
# ax3.axhline(y=150, color='w', lw=1, linestyle='--')
# # ax3.axhline(y=155, color='w', lw=1, linestyle='--')
# ax3.axhline(y=300, xmin=0.0, xmax=0.14, color='w', lw=2, linestyle='-')
# ax3.axhline(y=300, xmin=0.86, xmax=1.0, color='w', lw=2, linestyle='-')
# ax3.axhline(y=450, xmin=0.14, xmax=0.86, color='w', lw=2, linestyle='-')
# ax3.axvline(x=70, ymin=0.5, ymax=0.75, color='w', lw=2, linestyle='-')
# ax3.axvline(x=430, ymin=0.5, ymax=0.75, color='w', lw=2, linestyle='-')
# ax3.set_yticklabels(yticks)
# ax3.set_xticklabels(xticks)

plt.tight_layout()
plt.savefig('TE_test2.png')