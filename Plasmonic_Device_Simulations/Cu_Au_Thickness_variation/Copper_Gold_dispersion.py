import numpy as np
import matplotlib.pyplot as plt
import os

root = os.getcwd()

datafilename = '/Users/samblair/Desktop/Au_dispersion.csv'
datafilepath = os.path.join(
        root,
        datafilename)
wavg, ng, kg = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=1,
        unpack=True)

datafilename = '/Users/samblair/Desktop/Cu_dispersion.csv'
datafilepath = os.path.join(
        root,
        datafilename)
wavc, nc, kc = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=1,
        unpack=True)

datafilename = '/Users/samblair/Desktop/Ti_dispersion.csv'
datafilepath = os.path.join(
        root,
        datafilename)
wavt, nt, kt = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=1,
        unpack=True)

fig, ax = plt.subplots(figsize=[10,7])
ax.plot(wavg, ng, label='Gold n', color='gold', lw=3)
ax.plot(wavc, nc, label='Copper n', color='orange', lw=3)
ax.plot(wavt, nt, label='Titanium n', color='gray', lw=3)

ax2 = ax.twinx()
ax2.plot(wavg, kg, label='Gold k', color='gold', lw=3, linestyle='--')
ax2.plot(wavc, kc, label='Copper k', color='orange', lw=3, linestyle='--')
ax2.plot(wavt, kt, label='Titanium k', color='gray', lw=3, linestyle='--')

handles1, labels1 = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2

ax.set_xlabel('Wavelength (μm)', fontsize=20, color='k')
ax.set_ylabel('n', fontsize=20, color='k')
ax2.set_ylabel('k', fontsize=20, color='k')
ax.legend(handles, labels, loc='upper left', frameon=True, fontsize=15, labelcolor='k', ncols=2)
ax.tick_params(axis='both', labelsize=15, colors='k')
ax2.tick_params(axis='both', labelsize=15, colors='k')
plt.xlim([0.2,1.9])
plt.tight_layout()

plt.savefig('Cu_Au_dispersion.png')