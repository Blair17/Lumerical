import os
import numpy as np
import matplotlib.pyplot as plt

root = os.getcwd()

files_refl = '635_Optimised_OB_Sweep_Data/041223/data/refl/reflection0.24.txt'
files_phase = '635_Optimised_OB_Sweep_Data/041223/data/phase/phase0.24.txt'

datafilename = files_refl
datafilepath = os.path.join(
        root,
        datafilename)
l = np.genfromtxt(
        fname=datafilepath,
        delimiter=" ",
        skip_header=1,
        unpack=True)

datafilename = files_phase
datafilepath = os.path.join(
        root,
        datafilename)
p = np.genfromtxt(
        fname=datafilepath,
        delimiter=" ",
        skip_header=1,
        unpack=True)

x = np.linspace(615, 655, 1000)

fig, ax = plt.subplots()
ax.plot(x, l)
# ax.plot(x, p)

plt.savefig('test.png')


