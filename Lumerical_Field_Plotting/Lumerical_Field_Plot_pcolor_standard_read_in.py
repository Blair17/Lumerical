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

lam = 550
root = os.getcwd()

datafilename = f'/Volumes/Sam/Lumerical/Plasmonics/Gold_nanoballs/field_on_resonance_zoomed.txt'
datafilepath = os.path.join(
    root,
    datafilename)
field1 = np.genfromtxt(
    fname=datafilepath,
    delimiter=" ",
    skip_header=1,
    unpack=True)

# datafilename = '/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Updated_good_structure_scripts/Cu_Adhesion_Au_Antenna_plasmonic_device/index_cu_adhesion.txt'
# datafilepath = os.path.join(
#     root,
#     datafilename)
# field_r = np.genfromtxt(
#     fname=datafilepath,
#     delimiter=" ",
#     skip_header=1,
#     unpack=True)

# y_tick_loc = [0, 125, 250, 375, 500] # x = 51
# x_tick_loc = [125, 250, 375] # x = 51
# yticks = ['-50', '-25', '0', '25', '50']
# xticks = ['-50', '0', '50']

# x = 440, z = 100

fig, ax1 = plt.subplots(figsize=[10,7])
mycmap1 = plt.get_cmap('jet')

k = ax1.imshow((field1)*(1), 
              cmap=mycmap1,
              aspect='auto', 
              extent=[0, 500, 0, 500],
              interpolation='bicubic',
              origin='lower')
# ax1.contour(field_r, levels=np.linspace(0,100,150), 
#             extent=[0, 500, 0, 500], 
#             colors='w', linewidths=2, alpha=1)
ax1.set_xlabel('X [nm]', fontsize=24, fontweight='bold')
ax1.set_ylabel('Z [nm]', fontsize=24, fontweight='bold')
ax1.tick_params(axis='both', labelsize=18)
cbar = add_colorbar(k)
cbar.ax.set_title('E (V/m)', fontsize=22, fontweight='bold')
cbar.ax.tick_params(labelsize=22)
# ax1.set_yticks(y_tick_loc)
# ax1.set_xticks(x_tick_loc)
# ax1.set_yticklabels(yticks)
# ax1.set_xticklabels(xticks)

# ax1.axhline(y=170, xmin=0, xmax=1, color='w', lw=2, linestyle='-')
# ax1.axhline(y=197, xmin=0.34, xmax=0.66, color='k', lw=2, linestyle='--')

# plt.text(50, 400, 'Air',  color='white', fontweight='bold', fontsize=25, ha='center', va='center')
# plt.text(250, 350, 'Cu',  color='white', fontweight='bold', fontsize=25, ha='center', va='center')
# plt.text(50, 151, 'ITO',  color='white', fontweight='bold', fontsize=25, ha='center', va='center')
# plt.text(50, 185, r'$\bf{{Al_{2}}{O_{3}}}$',  color='white', fontweight='bold', fontsize=23, ha='center', va='center')
# plt.text(50, 60, 'Au',  color='white', fontweight='bold', fontsize=25, ha='center', va='center')

# plt.xlim([150, 350])
# plt.ylim([100, 450])
plt.tight_layout()
plt.savefig(f'field.png')

# fig, ax = plt.subplots()
# ax.pcolor(field_r)
# plt.savefig('index.png')