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

# # phase_pi = []
# # for q in r_array:
# #     if min(q) < 0:
# #         s = q + abs(min(q))
# #     else:
# #         s = q - abs(min(q))
# #     phase_pi.append((s / np.pi) )

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


# labels = ['600 - 800 nm', '500 - 700 nm', '630 - 660 nm', '550 - 700 nm', '500 - 1000 nm', '600 - 700 nm', '630 - 670 nm']

# fig, ax = plt.subplots(figsize=[10,7])
# for index, l in enumerate(l_array):
#     ax.plot(l,phase_pi[index], label=[x for x in labels][index])
#     ax.set_xlabel('Wavelength [nm]', fontsize=16, fontweight='bold')
#     ax.set_ylabel('Phase [π rad]', fontsize=16, fontweight='bold')
#     # ax.set_ylim([0, 1.0])
#     ax.set_xlim([600,700])
#     ax.tick_params(axis='both', labelsize=14)
#     ax.legend(frameon=True, loc=0, prop={'size': 14})
#     plt.title('Wavelength Range Variation', fontsize=18, fontweight='bold')
#     # plt.savefig('/Volumes/Sam/Lumerical/New/thickness_phase_tests/Phase/Phase_Variation.png')
#     # plt.axvline(x=0.665, color='k', lw=2, linestyle='--')
# # ax.plot(p[0],r_array[0], label=[x for x in labels][0])
# # ax.plot(p[1],r_array[1], label=[x for x in labels][1])
# # ax.plot(p[2],r_array[2], label=[x for x in labels][2])
# # ax.plot(p[-1],r_array[-1], label=[x for x in labels][-1])
# # ax.legend(frameon=True, loc=0, prop={'size': 14})

# plt.tight_layout()
# plt.show()