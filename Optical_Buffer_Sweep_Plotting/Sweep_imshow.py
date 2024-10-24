import os
import numpy as np
import matplotlib.pyplot as plt
import glob
from matplotlib.pyplot import cm
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits import axes_grid1

def last_9chars(x):
    return(x[-8:])

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

files_refl = glob.glob('/Volumes/Sam/Lumerical/Thorpe_paper_simulations/test_structure/Alox_thickness_loops/gold/data/refl/*.txt')
sorted_refl = sorted(files_refl, key = last_9chars)  

files_phase = glob.glob('/Volumes/Sam/Lumerical/Thorpe_paper_simulations/test_structure/Alox_thickness_loops/gold/data/phase/*.txt')
sorted_phase = sorted(files_phase, key = last_9chars)  

l_array = []
p_array = []

for file in sorted_refl:
    datafilename = file
    datafilepath = os.path.join(
        root,
        datafilename)
    l = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=1,
        unpack=True)
    l_array.append(l) 
    
for file in sorted_phase:
    datafilename = file
    datafilepath = os.path.join(
        root,
        datafilename)
    p = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=1,
        unpack=True)
    p_array.append(p) 

l_array = np.array(l_array)
p_array = np.array(p_array)

x = np.linspace(700, 1000, 1000)
y = np.linspace(0, 200, 51)

rnge = np.arange(0, 51, 1)
high_refl = []
phase_vals = []
d = []

# for r in rnge:
#         if min(l_array[r, :]) > 0.7:
#             high_refl.append(r)
#             # phase_vals.append(high_refl[r])
#         c = np.unwrap(p_array[r, :], period=np.pi)
#         d.append(c) 

l_array = np.fliplr(np.flipud((l_array)))
p_array = np.fliplr(np.flipud((p_array)))

s1 = np.array([q / np.pi for q in p_array])
s = np.array([k - min(k) for k in s1])

yticks = [25, 50, 75, 100]
yticklabels = ['50', '100', '150', '200']

xticks = [0, 25, 50, 75, 100]
xticklabels = ['700', '775', '850', '925', '1000']

xticksplot = [0, 200, 400, 600, 800, 1000]
xtickplotlabels = ['700', '760', '820', '880', '940', '1000']

# xticksplot = [600, 700, 800, 900]
# xtickplotlabels = ['880', '910', '940', '970']

color1 = iter(cm.jet(np.linspace(0, 1, len(high_refl))))
opt_buffer_values = np.linspace(0, 0.5, 101)
mycmap1 = plt.get_cmap('jet')

fig, ax = plt.subplots(2, 2, figsize=[10,7])
k = ax[0,0].imshow(l_array, 
              cmap=mycmap1,
              aspect='auto', 
              extent=[0, 100, 0, 100],
              interpolation='bicubic', origin='lower')
ax[0,0].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
ax[0,0].set_ylabel(r'Al$\mathbf{_2}$O$\mathbf{_3}$ Thickness [nm]', fontsize=16, fontweight='bold')
ax[0,0].set_yticks(yticks)
ax[0,0].set_yticklabels(yticklabels)
ax[0,0].set_xticks(xticks)
ax[0,0].set_xticklabels(xticklabels)
ax[0,0].tick_params(axis='both', labelsize=14)
cbar = add_colorbar(k)
cbar.ax.set_title('Refl', fontsize=14, fontweight='bold', pad=10)
cbar.ax.set_yticks(ticks=[np.amax(l_array),np.amin(l_array)], 
               labels=['100', '0'], fontsize=14)

# for i in range(len(l_array)):
    # ax[0,1].plot(l_array[i,:], label=i)
ax[0,1].plot(l_array[25,:], c='k')
# ax[0,1].plot(l_array[10,:], c='r')
# ax[0,1].legend(frameon=True, loc='lower left', ncol=2, fontsize=11)
ax[0,1].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
ax[0,1].set_ylabel('Reflection [%]', fontsize=16, fontweight='bold')
ax[0,1].set_ylim(0, 1.05)
ax[0,1].tick_params(axis='both', labelsize=14)
ax[0,1].set_xticks(xticksplot)
ax[0,1].set_xticklabels(xtickplotlabels)
# ax[0,1].set_ylim(0, 1)
ax[0,1].set_xlim(0, 1000)
ax[0,1].legend(frameon=True, loc='lower left', ncol=5, fontsize=8)

# fig, ax = plt.subplots(2, 2, figsize=[10,7])
k = ax[1,0].imshow((s), 
              cmap=mycmap1,
              aspect='auto', 
              extent=[0, 100, 0, 100],
              interpolation='bicubic', origin='lower')
ax[1,0].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
ax[1,0].set_ylabel('Oxide Thickness [μm]', fontsize=16, fontweight='bold')
ax[1,0].set_yticks(yticks)
ax[1,0].set_yticklabels(yticklabels)
ax[1,0].set_xticks(xticks)
ax[1,0].set_xticklabels(xticklabels)
ax[1,0].tick_params(axis='both', labelsize=14)
cbar = add_colorbar(k)
cbar.ax.set_title('Phase', fontsize=14, fontweight='bold', pad=10)
cbar.ax.set_yticks(ticks=[np.amax(s),np.amin(s)], 
               labels=[np.round(np.amax(s),2), np.round(np.amin(s),2)], fontsize=18)

ax[1,1].plot(s[1,:], c='k', linestyle='--')
ax[1,1].plot(s[10,:], c='r', linestyle='--')
# ax[0,1].legend(frameon=True, loc='lower left', ncol=2, fontsize=11)
ax[1,1].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
ax[1,1].set_ylabel('Phase [rad/π]', fontsize=16, fontweight='bold')
# ax[1,1].set_ylim(0, 1.05)
ax[1,1].tick_params(axis='both', labelsize=14)
ax[1,1].set_xticks(xticksplot)
ax[1,1].set_xticklabels(xtickplotlabels)
# ax[1,1].set_ylim(1, 5)
ax[1,1].set_xlim(0, 1000)

plt.tight_layout()
plt.savefig('test_structure_au.png')
# plt.show()