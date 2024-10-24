import os
import numpy as np
import matplotlib.pyplot as plt
import glob
from scipy.interpolate import LinearNDInterpolator
from Paluras_cmap import palura_colormap

def last_9chars(x):
    return(x[-8:])

def interpolate(x, y, array):
    # x = np.linspace(610, 660, 1000)
    # y = np.linspace(0, 1.0, 101)
    X, Y = np.meshgrid(x, y)
    x_interp = np.linspace(760, 800, 1000)
    y_interp = np.linspace(0, 0.1, 21)
    points = np.column_stack((X.ravel(), Y.ravel()))
    
    interp_func = LinearNDInterpolator(points, array.ravel())
    
    X_interp, Y_interp = np.meshgrid(x_interp, y_interp)
    points_interp = np.column_stack((X_interp.ravel(), Y_interp.ravel()))
    Z_interp = interp_func(points_interp)
    
    # Reshape Z_interp back to the 2D shape
    Z_interp = Z_interp.reshape(X_interp.shape)
    
    return(X_interp, Y_interp, Z_interp)

root = os.getcwd()

files_refl = glob.glob('/Volumes/Sam/Lumerical/Mie/array_angle_variation/TM/data/refl/*.txt')
sorted_refl = sorted(files_refl, key = last_9chars)  

files_phase = glob.glob('/Volumes/Sam/Lumerical/Mie/array_angle_variation/TM/data/phase/*.txt')
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
    

datafilename = '/Volumes/Sam/Lumerical/Mie/array_angle_variation/TM/data/wav/wavelength.txt'
datafilepath = os.path.join(
        root,
        datafilename)
wav = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=1,
        unpack=True)

l_array = np.array(l_array)
p_array = np.array(p_array)

x = np.linspace(1.240, 1.330, 2000)   
y = np.linspace(0, 20, 10)

rnge = np.arange(0, 20, 1)
high_refl = []
phase_vals = []
d = []

# for r in rnge:
#         if min(z_l[r, :]) > 0.7:
#             high_refl.append(r)
#             # phase_vals.append(high_refl[r])
#         c = np.unwrap(z_p[r, :], period=np.pi)
#         d.append(c) 

l_array = np.array(l_array).T
p_array = np.array(p_array).T

s1 = np.array([q / np.pi for q in p_array])
s = np.array([k - min(k) for k in s1])

fig, ax = plt.subplots(1,1, figsize=[10,7])
c = ax.imshow(l_array, aspect='auto', extent=[min(y), max(y), min(x), max(x)], cmap=palura_colormap())
ax.set_ylabel('Wavelength [μm]', fontsize=20, fontweight='bold')
ax.set_xlabel('Incident Angle [°]', fontsize=20, fontweight='bold')
ax.tick_params(axis='both', labelsize=18)

cbar = fig.colorbar(c, ax=ax) #, pad = 0.13)
cbar.set_label('Transmission [%]', size=20, fontweight='bold', rotation=270)
cbar.set_ticks(ticks=[np.amax(l_array),np.amin(l_array)], 
               labels=['100', '0'], fontsize=18)

# d = ax[1].imshow(s, aspect='auto', extent=[min(y), max(y), min(x), max(x)], cmap=palura_colormap())
# ax[1].set_ylabel('Wavelength [μm]', fontsize=20, fontweight='bold')
# ax[1].set_xlabel('Incident Angle [°]', fontsize=20, fontweight='bold')
# ax[1].tick_params(axis='both', labelsize=18)
# cbar = fig.colorbar(d, ax=ax[1]) #, pad = 0.13)
# # ax[1,0].set_xlim([617, 654])
# cbar.set_label('Phase [π/rad]', size=20, fontweight='bold', rotation=270)
# cbar.set_ticks(ticks=[np.amax(s),np.amin(s)], 
#                labels=[f'{np.round(np.amax(s),0)}', 
#                        f'{np.round(np.amin(s),2)}'],
#                          fontsize=18)

# for i, k in zip(high_refl, color1):
#     ax[0,1].plot(z_l[i], c=k, label=f'{opt_buffer_values[i].round(3)} μm')
#     ax[0,1].legend(frameon=True, loc='lower left', ncol=2, fontsize=11)
#     ax[0,1].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
#     ax[0,1].set_ylabel('Reflection [%]', fontsize=16, fontweight='bold')
#     ax[0,1].set_ylim(0, 1.05)
#     ax[0,1].tick_params(axis='both', labelsize=14)
#     ax[0,1].set_xticklabels(x_ticks)
    
#     ax[1,1].plot(s[i], c=k, label=f'{opt_buffer_values[i].round(3)} um')
#     ax[1,1].legend(frameon=True, loc='lower left', ncol=2, fontsize=11)
#     ax[1,1].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
#     ax[1,1].set_ylabel('Phase [π/rad]', fontsize=16, fontweight='bold')
#     ax[1,1].tick_params(axis='both', labelsize=14)
#     ax[1,1].set_xticklabels(x_ticks)

plt.tight_layout()
plt.savefig('Mie_Angle_Variation.png')

print(l_array.shape)

slice = l_array[:, 0]
fig, ax = plt.subplots()
ax.plot(slice)
plt.savefig('text.png')