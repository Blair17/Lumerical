import numpy as np
import matplotlib.pyplot as plt

e = 1.6E-19
e0 = 8.85E-12
me = 9.11E-31

N = 3E20 # cm^-3
gamma = 0.1185 * e # eV
me_star = 0.35 * me
eps_inf = 3.9
omega_p_sq = 1.0974 * e # eV

# o_p_sq = np.sqrt( (N * e**2) / (e0 *  me) )

wav_range = np.linspace(1.2, 1.8, 1000)
freq = [( 3E8 / (w * 1E6) ) * 1E12 for w in wav_range]
omega = [2 * np.pi * f for f in freq]
omega_sq = [w ** 2 for w in omega]

eps_drude = [eps_inf - (omega_p_sq / (o**2 + (1j * gamma * o))) for o in omega]

print(np.real(eps_drude))

plt.plot(wav_range, np.real(eps_drude), label='Real')  
# plt.show()