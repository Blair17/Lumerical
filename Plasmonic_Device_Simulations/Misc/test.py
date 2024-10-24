import numpy as np
import matplotlib.pyplot as plt
import os

root = os.getcwd()

file = '/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Au_Al2O3_ITO/Al2O3_Layer_Inv/nacc_sweeps/30nm_Buffer/data/refl/reflection2.00.txt'
file2 = '/Volumes/Sam/Lumerical/Plasmonics/visible_metasurface_plasmonic/Au_Al2O3_ITO/Al2O3_Layer_Inv/nacc_sweeps/30nm_Buffer/data/phase/phase2.00.txt'

datafilename = file
datafilepath = os.path.join(
        root,
        datafilename)
l = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=1,
        unpack=True)

datafilename = file2
datafilepath = os.path.join(
        root,
        datafilename)
p = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=1,
        unpack=True)

wav = np.linspace(500,1000,1000)

fig, ax = plt.subplots()
ax.plot(wav, l[::-1])
plt.savefig('testing.png')
plt.show()
