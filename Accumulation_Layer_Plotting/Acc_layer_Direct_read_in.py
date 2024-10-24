import os
import numpy as np
import matplotlib.pyplot as plt
import glob
from scipy.interpolate import LinearNDInterpolator
from matplotlib.pyplot import cm
import pandas as pd

def last_9chars(x):
    return(x[-8:])

def find_closest_value(array, target_value):
    index = np.abs(array - target_value).argmin()
    closest_value = array[index]
    return index, closest_value

root = os.getcwd()
 
datafilename = '/Volumes/Sam/Lumerical/Atwater_modulator/test_design/nacc1.9_R.txt'
datafilepath = os.path.join(
        root,
        datafilename)
wav1, R1 = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=2,
        unpack=True)

datafilename = '/Volumes/Sam/Lumerical/Atwater_modulator/test_design/nacc2.0_R.txt'
datafilepath = os.path.join(
        root,
        datafilename)
wav2, R2 = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=2,
        unpack=True)

datafilename = '/Volumes/Sam/Lumerical/Atwater_modulator/test_design/nacc2.1_R.txt'
datafilepath = os.path.join(
        root,
        datafilename)
wav3, R3 = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=2,
        unpack=True)

datafilename = '/Volumes/Sam/Lumerical/Atwater_modulator/test_design/nacc1.9_S.txt'
datafilepath = os.path.join(
        root,
        datafilename)
wav1, S1 = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=2,
        unpack=True)

datafilename = '/Volumes/Sam/Lumerical/Atwater_modulator/test_design/nacc2.0_S.txt'
datafilepath = os.path.join(
        root,
        datafilename)
wav2, S2 = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=2,
        unpack=True)

datafilename = '/Volumes/Sam/Lumerical/Atwater_modulator/test_design/nacc2.1_S.txt'
datafilepath = os.path.join(
        root,
        datafilename)
wav3, S3 = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=2,
        unpack=True)



fig, ax = plt.subplots()
ax.plot(wav1, R1, label='1.9', color='r', lw=2, alpha=0.5)
ax.plot(wav2, R2, label='2.0', color='b', lw=2, alpha=0.5)
ax.plot(wav3, R3, label='2.1', color='g', lw=2)

plt.tight_layout()
plt.savefig('refl.png', dpi=300)

fig, ax = plt.subplots()
ax.plot(wav1, S1, label='1.9', color='r', lw=2, alpha=0.5)
ax.plot(wav2, S2, label='2.0', color='b', lw=2, alpha=0.5)
ax.plot(wav3, S3, label='2.1', color='g', lw=2)

plt.tight_layout()
plt.savefig('phase.png', dpi=300)
