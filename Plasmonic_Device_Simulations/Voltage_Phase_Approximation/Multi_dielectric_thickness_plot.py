import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'nature', 'std-colors'])

voltage = np.arange(0,51,1) # V
eps_0 = 8.85E-12 # F/m
eps_r = 22
# d = 10E-09 # m dielectric
w = 1E-09 # m accumulation
e = 1.6E-19 # C
n_zero = 1.25E+25 # m^-3

spacer_array = [1, 5, 10, 15, 20, 30, 40, 50, 100]

c = 3E8
eps_inf = 3.9
m_e = 9.11E-31
m_star = m_e * 0.5
omega = ( 2 * np.pi * c) / 800E-09
gamma = 3.9E14 # Hz

index_array = []

for d in spacer_array:
    d = d * 1E-09
    m_2 = [ ( eps_0 * eps_r * ( v / (d*e) ) ) for v in voltage] # m^-2
    N_m3 = [n_zero + (n / w) for n in m_2]

    omega_p_sqs = [(N * (e ** 2)) / (eps_0 * m_star) for N in N_m3]
    eps_drude = [eps_inf - (omp / complex(omega**2,gamma*omega)) for omp in omega_p_sqs]

    n_riu = [ np.sqrt ( (np.sqrt((e.real)**2 + (e.imag)**2) + e.real) / 2 ) for e in eps_drude]
    
    index_array.append(n_riu)

y_tick_locs = [0.8, 1.2, 1.6, 2.0]

y1 = n_riu[0]
y2 = n_riu[15]
print(np.abs(y2-y1))

labels = [f'{d} nm' for d in spacer_array]

pparam = dict(xlabel='Voltage (V)', ylabel='Refractive index (RIU)')

fig, ax = plt.subplots()
for s in range(len(index_array)):
    ax.plot(voltage, index_array[s], label=labels[s])
ax.legend(loc='lower right')
ax.autoscale(tight=True)
ax.set(**pparam)
# ax.set_xlim([0,30])
ax.set_ylim([1.0, 2.0])
# fig.text(0.4,0.9,f'Wavelength = 2$\mu$m', fontsize=7, fontweight='bold', transform=ax.transAxes)
fig.savefig('spacer_variation_HAOL_voltage.png', dpi=300)
plt.close()











