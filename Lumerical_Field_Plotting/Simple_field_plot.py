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

datafilename = f'/Volumes/Sam/Lumerical/Thorpe_paper_simulations/test_structure/new_field.txt'
datafilepath = os.path.join(
    root,
    datafilename)
field1 = np.genfromtxt(
    fname=datafilepath,
    delimiter="",
    skip_header=1,
    unpack=True)

datafilename = '/Volumes/Sam/Lumerical/Thorpe_paper_simulations/test_structure/new_index_base.txt'
datafilepath = os.path.join(
    root,
    datafilename)
contour_base = np.genfromtxt(
    fname=datafilepath,
    delimiter="",
    skip_header=1,
    unpack=True)

datafilename = '/Volumes/Sam/Lumerical/Thorpe_paper_simulations/test_structure/new_index.txt'
datafilepath = os.path.join(
    root,
    datafilename)
contour = np.genfromtxt(
    fname=datafilepath,
    delimiter="",
    skip_header=1,
    unpack=True)

maskITO = contour > 1
# t = contour_base < 1.2

# field_masked = field1 * t * maskITO
summed_ITO = np.sum(field1)

# data_ITO = (np.sum(np.abs(field_masked)) / np.sum(np.abs(field1)) )
# print(data_ITO)

# fig, ax = plt.subplots()
# ax.imshow(np.flipud(field_masked))
# plt.show()

y_tick_loc = [0, 250, 500] # x = 51
x_tick_loc = [50, 250, 450] # x = 51
yticks = ['-250', '0', '250']
xticks = ['-200', '0', '200']

# x = 440, z = 100
plt.style.use("dark_background")
field1 = field1 / np.max(field1)

fig, ax1 = plt.subplots(figsize=[10,7])
mycmap1 = plt.get_cmap('jet')

# maskITO = contour > 1
# t = contour < 1.2
# field_masked = field1 * t * maskITO
# data_ITO = (np.sum(np.abs(field_masked)) / np.sum(np.abs(field1)) )

k = ax1.imshow((field1), 
              cmap=mycmap1,
              aspect='auto', 
              extent=[0, 500, 0, 500],
              interpolation='bicubic',
              origin='lower')
ax1.contour(contour_base, levels=np.linspace(0,1,100), 
            extent=[0, 500, 0, 500], 
            colors='w', linewidths=2, alpha=1)
ax1.contour(contour, levels=2, 
            extent=[0, 500, 0, 500], 
            colors='w', linewidths=2, alpha=1)
# ax1.set_xlabel('X [nm]', fontsize=32, fontweight='bold')
# ax1.set_ylabel('Z [nm]', fontsize=32, fontweight='bold')
# ax1.tick_params(axis='both', labelsize=18)
cbar = add_colorbar(k)
cbar.ax.set_title('|E|', fontsize=32, fontweight='bold', pad=22)
cbar.ax.tick_params(labelsize=30)
ax1.set_yticks(y_tick_loc)
ax1.set_xticks(x_tick_loc)
ax1.set_yticklabels(yticks, size=32)
ax1.set_xticklabels(xticks, size=32)

# plt.xlim([150, 350])
# plt.ylim([100, 450])
plt.tight_layout()
plt.savefig(f'Field1.png', dpi=300)

fig, ax = plt.subplots()
ax.imshow(np.flipud(contour_base))
plt.savefig('index.png')