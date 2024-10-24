import os
import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
import pandas as pd
np.set_printoptions(threshold=sys.maxsize)

root = os.getcwd()

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

def tick_function(X):
    '''
    Converts frequency ticks to wavelength ticks, converts from Hz to μm.
    Args:
        X: [array] array of x ticks to convert
    Returns:
        ["%.0f" % z for z in V]: [array] array of converted X ticks.
    '''
    c=3E8
    V = (c/(X * 1E12)) * 1E6
    return ["%.2f" % z for z in V]

''' Conductivity '''
sigmas = 1260.9 # S/cm
mu = 1 # cm^2/Vs
# eps_inf = np.arange(1,8,2)
eps_inf = [5.42]

''' Omega P Squared '''
c = 3E8 # ms-1
e = 1.6E-19 # C
m_e = 9.11E-31 # kg
# m_star = m_e * 0.3 # kg
m_star = m_e * 0.5 # kg
eps_0 = 8.85E-12 # CV-1m-1
gamma = 2E+14
# gamma = 2E+14

''' Calculate N from sigmas '''
# N_m3 = (sigmas / (mu * e)) * 1E6 # m^-3
# N_m3 = 2.77E+27
N_m3 = 1.25E+25
# omega_p_sqs = (N_m3 * (e ** 2)) / (eps_0 * m_star) # rad/s
# omega_p_sq_radTHz = (np.sqrt(omega_p_sqs) / (2 * np.pi)) / 1E12 # THz

radTHz = 360
radHz = radTHz * 1E+12
omega_p_sqs = (radHz * 2 * np.pi) ** 2

# radTHz = 1351
# radHz = radTHz * 1E+12
# omega_p_sqs = (radHz * 2 * np.pi) ** 2

print(omega_p_sqs)

''' Wavelength '''
frequency_THz = np.arange(1000, 1, -1)
frequency = [f * 1E12 for f in frequency_THz]
wavrange = [c / f * 1E9 for f in frequency]
omega = [2 * np.pi * f for f in frequency]
omega_sq = [w ** 2 for w in omega]

''' Drude '''
eps_drude = []
for eps_infty in eps_inf:
    eps_drude.append([eps_infty - (omega_p_sqs / w) for w in omega_sq])
    
eps_imag = []
for eps_infty in eps_inf:
    eps_imag.append([ ( eps_infty * omega_p_sqs) /  ( w * gamma ) / 100 for w in omega])

ticks = [10, 120, 240, 360, 480, 600]
ticks_y = [-6]
ticks2 = [100, 200, 300, 400, 500, 600]
ticks3 = ['0.50', '0.60', '0.75', '1.00', '1.50', '3.00']

''' Plot '''
colors = len(eps_inf)
cmap = plt.cm.rainbow(np.linspace(0,1,colors))
fig, ax1 = plt.subplots(nrows=1, ncols=1, figsize=[10, 7])
ax2 = ax1.twiny()
for eps, i, index in zip(eps_drude,range(colors),eps_inf):
    ax1.plot(frequency_THz, eps, lw=4, color=cmap[i], label=f'$\epsilon_\infty$={index}')

ax3 = ax1.twiny()
for eps, i, index in zip(eps_imag,range(colors),eps_inf):
    ax3.plot(frequency_THz, eps[::-1], lw=4, color=cmap[i], label=f'$\epsilon_\infty$={index}')

ax1.axhline(y=0, color='k', lw=2, linestyle='--', alpha=0.5)
# ax1.legend(loc='lower left', ncol=2, prop={'size': 22})
ax1.set_ylim(-20, 20)

ax2.set_xticks(ticks)
ax1.set_ylim(-1.7, 5.9)
ax2.set_xlim(0, 600)
ax2Ticks = ax2.get_xticks()
ax2.set_xticklabels(ticks)
ax1Ticks = ax2Ticks
ax1.set_xticks(ax1Ticks)
ax1.set_xbound(ax2.get_xbound())
ax1.tick_params(axis='both', labelsize=(28))
ax2.tick_params(axis='both', labelsize=(28))
ax1.set_xticklabels(tick_function(ax1Ticks))
ax2.set_xlabel("Frequency (THz)", fontsize=(32), fontweight='bold', labelpad=20)
ax1.set_xlabel("Wavelength (μm)", fontsize=(32), fontweight='bold')
ax1.set_ylabel(r'$\bf{\epsilon_{r}}$ (a.u.)', fontsize=(28), fontweight='bold') 
    
ax1.yaxis.set_major_locator(MultipleLocator(2))
ax1.yaxis.set_minor_locator(AutoMinorLocator())
ax2.xaxis.set_minor_locator(AutoMinorLocator())
ax1.xaxis.set_minor_locator(AutoMinorLocator())

ax1.invert_xaxis()
ax2.invert_xaxis()

plt.tight_layout()
plt.savefig('Fig4b.png')  

zeros = np.zeros(len(wavrange))
print(len(eps_imag))
print(len(eps_drude))

df = pd.DataFrame({"Wavelength (nm)" : wavrange, "Permittivity" : eps_drude[0], "Loss" : eps_imag[0]})
df.to_csv('Permittivity_data.csv', index=False)


# print(eps_drude)
# print(f'Conductivity = {sigmas} \n Mobility = {mu} \n N = {N_m3} \n Omega P Squared rad/s= {omega_p_sqs} \n omega_P Squared radTHz = {omega_p_sq_radTHz}')