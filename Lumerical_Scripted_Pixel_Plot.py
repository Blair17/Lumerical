import os
import numpy as np
import matplotlib.pyplot as plt
import glob
from scipy.interpolate import LinearNDInterpolator
from matplotlib.pyplot import cm

def last_9chars(x):
    return(x[-8:])

def interpolate(x, y, array):
    # x = np.linspace(610, 660, 1000)
    # y = np.linspace(0, 1.0, 101)
    X, Y = np.meshgrid(x, y)
    x_interp = np.linspace(615, 655, 1000)
    y_interp = np.linspace(0.0, 1.00, 101)
    points = np.column_stack((X.ravel(), Y.ravel()))
    
    interp_func = LinearNDInterpolator(points, array.ravel())
    
    X_interp, Y_interp = np.meshgrid(x_interp, y_interp)
    points_interp = np.column_stack((X_interp.ravel(), Y_interp.ravel()))
    Z_interp = interp_func(points_interp)
    
    # Reshape Z_interp back to the 2D shape
    Z_interp = Z_interp.reshape(X_interp.shape)
    
    return(X_interp, Y_interp, Z_interp)

root = os.getcwd()

files_refl = glob.glob('/Volumes/Sam/Lumerical/Scripting/051223/data/refl/*.txt')
sorted_refl = sorted(files_refl, key = last_9chars)  

files_phase = glob.glob('/Volumes/Sam/Lumerical/Scripting/051223/data/phase/*.txt')
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
        
x = np.linspace(615, 655, 1000)
y = np.linspace(0, 1.00, 101)

x_l, y_l, z_l = interpolate(x, y, l_array)
x_p, y_p, z_p = interpolate(x, y, p_array)

rnge = np.arange(0, 101, 1)
high_refl = []
phase_vals = []
d = []

for r in rnge:
        if min(z_l[r, :]) > 0.7:
            high_refl.append(r)
            # phase_vals.append(high_refl[r])
        c = np.unwrap(z_p[r, :], period=np.pi)
        d.append(c) 

s1 = np.array([q / np.pi for q in d])
s = np.array([k - min(k) for k in s1])

color1 = iter(cm.jet(np.linspace(0, 1, len(high_refl))))
opt_buffer_values = np.linspace(0, 1.0, 101)
x_ticks = ['605', '615', '625', '625', '635', '645', '655']

fig, ax = plt.subplots(2, 2, figsize=[10,7])
c = ax[0,0].pcolor(x_l, y_l, z_l, cmap='jet')
ax[0,0].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
ax[0,0].set_ylabel('Oxide Thickness [μm]', fontsize=16, fontweight='bold')
ax[0,0].tick_params(axis='both', labelsize=14)
cbar = fig.colorbar(c, ax=ax[0,0]) #, pad = 0.13)
ax[0,0].set_xlim([617, 654])
cbar.set_label('Reflection [%]', size=16, fontweight='bold', rotation=270)
cbar.set_ticks(ticks=[np.amax(z_l),np.amin(z_l)], 
               labels=['100', '0'], fontsize=18)

for i, k in zip(high_refl, color1):
    ax[0,1].plot(z_l[i], c=k, label=f'{opt_buffer_values[i].round(3)} μm')
    ax[0,1].legend(frameon=True, loc='lower left', ncol=2, fontsize=11)
    ax[0,1].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
    ax[0,1].set_ylabel('Reflection [%]', fontsize=16, fontweight='bold')
    ax[0,1].set_ylim(0, 1.05)
    ax[0,1].tick_params(axis='both', labelsize=14)
    ax[0,1].set_xticklabels(x_ticks)
    
    ax[1,1].plot(s[i], c=k, label=f'{opt_buffer_values[i].round(3)} um')
    ax[1,1].legend(frameon=True, loc='lower left', ncol=2, fontsize=11)
    ax[1,1].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
    ax[1,1].set_ylabel('Phase [π/rad]', fontsize=16, fontweight='bold')
    ax[1,1].tick_params(axis='both', labelsize=14)
    ax[1,1].set_xticklabels(x_ticks)

c = ax[1,0].pcolor(x_p, y_p, s, cmap='plasma')
ax[1,0].set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
ax[1,0].set_ylabel('Oxide Thickness [μm]', fontsize=16, fontweight='bold')
ax[1,0].tick_params(axis='both', labelsize=14)
cbar = fig.colorbar(c, ax=ax[1,0]) #, pad = 0.13)
ax[1,0].set_xlim([617, 654])
cbar.set_label('Phase [π/rad]', size=18, fontweight='bold', rotation=270)
cbar.set_ticks(ticks=[np.amax(s),np.amin(s)], 
               labels=[f'{np.round(np.amax(s),0)}', 
                       f'{np.round(np.amin(s),2)}'],
                         fontsize=18)

plt.tight_layout()
plt.savefig('051223_GMRM.png')