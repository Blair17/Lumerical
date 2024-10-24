import matplotlib.pyplot as plt
import numpy as np
import os 
import scipy as scipy
import scipy.ndimage
import sys
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits import axes_grid1
import glob
np.set_printoptions(threshold=sys.maxsize)

def last_9chars(x):
    return(x[-13:])

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
    
datafilename = '/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Updated_good_structure_scripts/Ti_testing/field_Ti_testing_5nm_Ti.txt'
datafilepath = os.path.join(
    root,
    datafilename)
field1 = np.genfromtxt(
    fname=datafilepath,
    delimiter=" ",
    skip_header=1,
    unpack=True)  

datafilename = '/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Updated_good_structure_scripts/Ti_testing/index_Ti_testing_5nm_Ti.txt'
datafilepath = os.path.join(
        root,
        datafilename)
index1 = np.genfromtxt(
        fname=datafilepath,
        delimiter=" ",
        skip_header=1,
        unpack=True)

# x_tick_loc = [0, 10, 20, 30, 40] 
# y_tick_loc = [0, 87.5, 175, 262.5, 350]

xticks = ['-150', '-50', '50', '150']
# yticks = ['-250', '-150', '-50', '50', '150', '250']
# yticks = ['-500', '-250', '0', '250', '500']
yticks = ['-100', '-50', '0', '50', '100']
y_tick_loc = [0, 125, 250, 375, 500]
x_tick_loc = [100, 200, 300, 400]
# yticks = ['-30', '0', '30']

fig, ax1 = plt.subplots(figsize=[10,7])
mycmap1 = plt.get_cmap('hot')

# ax1.pcolor(field1, cmap=mycmap1)
# ax1.set_ylim([0, 500])
k = ax1.imshow(field1, 
                cmap=mycmap1,
                aspect='auto',
                extent=[0, 500, 0, 500],
                interpolation='bicubic',
                origin='lower')
ax1.contour(index1, levels=np.linspace(-20,15,20), 
                extent=[0, 500, 0, 500], 
                colors='w', linewidths=1.5, alpha=1)
# ax1.contour(index1, np.linspace(-1,79,100),
#                 # extent=[0, 500, 0, 500], 
#                 colors='w', linewidths=1.5, alpha=1)
ax1.set_xlabel('X (nm)', fontsize=24, fontweight='bold')
ax1.set_ylabel('Z (nm)', fontsize=24, fontweight='bold')
ax1.tick_params(axis='both', labelsize=25)
cbar = add_colorbar(k)
cbar.ax.set_title('|H| (A/m)', fontsize=22, fontweight='bold', pad=20)
# cbar.ax.set_title('Ey (V/m)', fontsize=22, fontweight='bold', pad=20)
cbar.ax.tick_params(labelsize=22)
ax1.set_xticks(x_tick_loc)
ax1.set_yticks(y_tick_loc)
ax1.set_yticklabels(yticks)
ax1.set_xticklabels(xticks)
ax1.set_ylim([120, 385])

# ax1.axhline(y=248, xmin=0.435, xmax=0.565, color='k', lw=1.5, linestyle='--')
ax1.axhline(y=250, color='w', lw=1.5, linestyle='-')
ax1.axhline(y=238, color='w', lw=1.5, linestyle='-')
# ax1.axhline(y=180, color='k', lw=1.5, linestyle='--')
# ax1.axhline(y=150, color='k', lw=3, linestyle='-')
# ax1.axhline(y=350, xmin=0.07, xmax=0.93, color='k', lw=3, linestyle='-')
# # ax1.axhline(y=19, color='k', lw=4, linestyle='-')

plt.text(40, 350, 'Air',  color='white', fontweight='bold', fontsize=25, ha='center', va='center')
plt.text(245, 320, 'Au',  color='white', fontweight='bold', fontsize=25, ha='center', va='center')
plt.text(40, 244, r'$\bf{{Al_{2}}{O_{3}}}$',  color='white', fontweight='bold', fontsize=20, ha='center', va='center')
plt.text(40, 230.5, 'ITO',  color='white', fontweight='bold', fontsize=20, ha='center', va='center')
# # plt.text(4, 100, r'$\bf{SiO_{2}}$',  color='white', fontweight='bold', fontsize=25, ha='center', va='center')
plt.text(40, 150, 'Au',  color='white', fontweight='bold', fontsize=25, ha='center', va='center')

# plt.ylim([120,300])
# plt.xlim([0, 40])

# plt.title(r'50 nm SiO$\bf{_{2}}$ Buffer', fontsize=24, fontweight='bold', pad=10)
# plt.arrow(7, 165, 0, 11, width=0.5, head_width=2, head_length=10, fc='w', ec='w')
# plt.arrow(9, 215, -0, -10, width=0.5, head_width=2, head_length=10, fc='w', ec='w')

plt.tight_layout()
plt.savefig(f'Plasmonic_TunMet_Ti_5nm_Layer.png', dpi=300)

# fig, ax = plt.subplots()
# ax.pcolor(index1)
# plt.savefig('index.png')