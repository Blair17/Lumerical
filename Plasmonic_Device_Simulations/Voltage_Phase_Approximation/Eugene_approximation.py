import numpy as np
import matplotlib.pyplot as plt

voltage = np.arange(0,51,1) # V
eps_0 = 8.85E-12 # F/m
eps_r = 9.34
d = 5E-09 # m dielectric
w = 1E-09 # m accumulation
e = 1.6E-19 # C
n_zero = 1.25E+25 # m^-3

c = 3E8
eps_inf = 3.9
m_e = 9.11E-31
m_star = m_e * 0.5
omega = ( 2 * np.pi * c) / 800E-09
gamma = 3.9E14 # Hz

m_2 = [ ( eps_0 * eps_r * ( v  / (d*e) ) ) for v in voltage] # m^-2
N_m3 = [n_zero + (n / w) for n in m_2]

omega_p_sqs = [(N * (e ** 2)) / (eps_0 * m_star) for N in N_m3]
eps_drude = [eps_inf - (omp / complex(omega**2,gamma*omega)) for omp in omega_p_sqs]

n_riu = [ np.sqrt ( (np.sqrt((e.real)**2 + (e.imag)**2) + e.real) / 2 ) for e in eps_drude]

# voltagezero = n_riu[35]
# voltage10 = n_riu[45]
# voltage20 = n_riu[55]
# voltage30 = n_riu[65]
# voltage35 = n_riu[70]

# print(f'Voltage 0 = {voltagezero}, \n Voltage 10 = {voltage10}, \n Voltage 20 = {voltage20}, \n Voltage 30 = {voltage30}, \n Voltage 35 = {voltage35}')

y_tick_locs = [0.8, 1.2, 1.6, 2.0]

y1 = n_riu[0]
y2 = n_riu[15]
# print(y2)
print(np.abs(y2-y1))

fig, ax = plt.subplots(figsize=[10,7])
# ax.plot(voltage, N_m3, lw=4, c='k', label='Carrier Density')
# ax.set_ylabel(r'Carrier Density (m$\bf{^{-3}}$)', fontsize=18, fontweight='bold')
# ax.tick_params(labelsize=15)

# ax = ax.twinx()
ax.plot(voltage, n_riu, lw=5, c='k', label='Refractive Index')
ax.set_xlabel('Voltage (V)', fontsize=30, fontweight='bold')
ax.set_ylabel('Refractive Index (RIU)', fontsize=30, fontweight='bold')
ax.tick_params(labelsize=27)
# ax.set_yticks(y_tick_locs)  
# ax.grid(which='major', axis='both', linestyle='--')
ax.set_xlim([0,20])
# ax.set_ylim([1.0, 2.0])

plt.text(0.5,0.8,f'Dielectric = {np.round(d*1E9,2)} nm', fontsize=25, transform=ax.transAxes)

# plt.grid(True)
plt.tight_layout()
plt.savefig('N_n_Approximation.png')
# plt.show()






