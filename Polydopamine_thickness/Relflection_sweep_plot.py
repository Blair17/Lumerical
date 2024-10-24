import numpy as np
import matplotlib.pyplot as plt
import scienceplots

import os
import numpy as np
import matplotlib.pyplot as plt
import glob
import scienceplots
plt.style.use(['science', 'nature', 'custom'])

def last_9chars(x):
    return(x[-12:])

root = os.getcwd()
files = glob.glob('/Volumes/Sam/Lumerical/TiO2_Inv/SiN_ITO_20nm_220724/650/*.txt')
sorted_array = sorted(files, key = last_9chars)  
print(sorted_array)

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
        skip_header=3,
        unpack=True)
    l_array.append(l)
    r_array.append(r)   

p = []
for k in l_array:
    p.append(k*1E6)

peaks = []

for i in range(len(l_array)):
    maxn2 = np.round( l_array[i][np.argmax(r_array[i])], 3)
    peaks.append(maxn2)
    
print(peaks)
    
pparam = dict(xlabel='Wavelength (nm)', ylabel=r'Reflection (\%)')

# labels = ['0 nm ITO, TE', '0 nm ITO, TM', '60 nm ITO, TE', '60 nm ITO, TM']
labels = ['TE 1.8', 'TM 1.8', 'TE 2.0', 'TM 2.0']

fig, ax = plt.subplots()
for i in range(len(r_array)):
    ax.plot(l_array[i], r_array[i]*100, label=labels[i])
ax.legend(loc=0, fontsize=6)
ax.autoscale(tight=True)
ax.set(**pparam)
ax.set_ylim([0, 100])
ax.set_xlim([600, 700])
fig.savefig('R_ITO_20nm_650.png', dpi=600)
plt.close()