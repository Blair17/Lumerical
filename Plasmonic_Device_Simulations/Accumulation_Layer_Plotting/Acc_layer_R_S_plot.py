import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import os
from matplotlib.pyplot import cm

def min_func(array):
    min_array = []
    for i in array:
        min_array.append(i - min(array))
    return min_array

root = os.getcwd()

datafilename = '/Users/samblair/Desktop/PhD/Admin/Conferences/SPIE_2024/Buffer_data/0nm_Buffer.csv'
datafilepath = os.path.join(
        root,
        datafilename)
nacc0, refl0, phase0 = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=1,
        unpack=True)

# datafilename = '/Users/samblair/Desktop/PhD/Admin/Conferences/SPIE_2024/30nm_Buffer.csv'
# datafilepath = os.path.join(
#         root,
#         datafilename)
# nacc30, refl30, phase30 = np.genfromtxt(
#         fname=datafilepath,
#         delimiter=",",
#         skip_header=1,
#         unpack=True)

# datafilename = '/Users/samblair/Desktop/PhD/Admin/Conferences/SPIE_2024/50nm_Buffer.csv'
# datafilepath = os.path.join(
#         root,
#         datafilename)
# nacc50, refl50, phase50 = np.genfromtxt(
#         fname=datafilepath,
#         delimiter=",",
#         skip_header=1,
#         unpack=True)

min0 = min_func(phase0)
# min30 = min_func(phase30)
# min50 = min_func(phase50)

y_tick_loc = [0, 0.5, 1.0, 1.50]

rnge = np.arange(0, 6, 1)

color1 = iter(cm.jet(np.linspace(0, 1, len(rnge))))
print(color1)
# cubic_interpolation_model = interp1d(nacc0, min0, kind = "cubic")
# X_ = np.linspace(nacc0.min(), nacc0.max(), 500)
# Y_ = cubic_interpolation_model(X_)

fig, ax = plt.subplots(figsize=[10,7])
ax.plot(nacc0, min0, lw=6, c='navy', linestyle='-', label='0 nm')
# ax.plot(X_,Y_, lw=4, c='r', linestyle='--')
# ax.plot(nacc30, min30, lw=6, c='greenyellow', linestyle='-', label='30 nm')
# ax.plot(nacc50, min50, lw=6, c='maroon', linestyle='-', label='50 nm')
ax.set_xlabel('Refractive Index (RIU)', fontsize=25, color='k', fontweight='bold')
ax.set_ylabel('Phase (rad/π)', fontsize=25, color='k', fontweight='bold')
ax.tick_params(axis='both', labelsize=25, colors='k')
ax.set_yticks(y_tick_loc)
# ax.legend(loc=0, frameon=True, fontsize=25, facecolor='w', framealpha=1)

plt.tight_layout()
# plt.grid()
plt.savefig('Phase_vs_index_plot_0nm.png', dpi=300, bbox_inches='tight')
#  31.50