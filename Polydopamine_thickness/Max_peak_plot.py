import os
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
import glob as glob

plt.style.use(['science', 'nature', 'std-colors'])

def last_9chars(x):
    return(x[-12:])

root = os.getcwd()

# files = glob.glob('/Volumes/Sam/Lumerical/Polydopamine_thickness_investigation/peak_thickness_index/*.txt')
files = glob.glob('/Volumes/Sam/Lumerical/Polydopamine_thickness_investigation/Higher_res_data/data/max_lam/*.txt')
# files = glob.glob('/Volumes/Sam/Lumerical/Polydopamine_thickness_investigation/data/max_lam/*.txt')
sorted_array = sorted(files, key = last_9chars)  

l_array = []
r_array = []

for file in sorted_array:
    datafilename = file
    datafilepath = os.path.join(
        root,
        datafilename)
    l, r = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=0,
        unpack=True)
    l_array.append(l)
    r_array.append(r)  

pparam = dict(xlabel= 'Thickness (nm)', ylabel='Wavelength (nm)')

# labels = ['1.3', '1.4', '1.5', '1.6', '1.7', '1.8']
labels = ['1.40', '1.45', '1.50', '1.55', '1.60', '1.65', '1.70']

fig, ax = plt.subplots()
for i in range(len(r_array)):
    # ax.scatter(l_array[i], r_array[i], marker='o', label=labels[i], s=10)
    ax.plot(l_array[i], r_array[i], label=labels[i])
ax.legend(loc='upper right', fontsize=7, frameon=True)
ax.autoscale(tight=True)
ax.set(**pparam)
# ax.tick_params(axis='both', labelsize=9)
# ax.set_ylabel('Wavelength (nm)', fontsize=9)
# ax.set_xlabel('Thickness (nm)', fontsize=9)
# ax.set_ylim([646, 649])
# ax.set_xlim([0,5])
fig.savefig('Thickness_vs_peak_high_res.png', dpi=600)
plt.close()