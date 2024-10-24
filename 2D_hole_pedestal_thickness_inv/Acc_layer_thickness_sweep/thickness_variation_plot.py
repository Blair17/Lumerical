import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def plot_field_max(filepath):
    def linear_func(x, m, c):
        return m * x + c
    
    root = os.getcwd()

    datafilepath = os.path.join(
        root,
        filepath)
    thickness, wav_max = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=0,
        unpack=True)
    
    wav_max = wav_max * 1E9
    
    T_array = np.linspace(1,10,10)
    colors = len(T_array)
    cmap = plt.cm.rainbow(np.linspace(0,1,colors))
    
    popt, pcov = curve_fit(linear_func, thickness, wav_max)
    slope, intercept = popt
    slope_error, intercept_error = pcov
    fit_line = linear_func(thickness, *popt)

    # for (t, f, c) in zip(thickness, field_max, range(colors)):
    fig, ax = plt.subplots(figsize=[10,5])
    ax.scatter(thickness, wav_max, color=cmap, s=200)
    ax.plot(thickness, fit_line, '--', lw=2, color='k', alpha=0.5)
    ax.set_xlabel('Accumulation Layer Thickness [nm]', fontsize=18, fontweight='bold')
    ax.set_ylabel('Resonant Wavelength [nm]', fontsize=18, fontweight='bold')
    ax.tick_params(axis='both', labelsize=18)
    ax.set_title('Accumulation Layer Thickness vs Resonant Wavelength', fontsize=20)
    ax.text(5, 736, f'Slope = {np.round(slope,4)} ± {np.round(slope_error[0],4)}', 
            fontsize=15, color='k')

    plt.tight_layout()
    plt.savefig('2D_hole_pedestal_thickness_inv/Acc_layer_thickness_sweep/Res_lambda_plot.png')

datafilename = '/Volumes/Sam/Lumerical/2D_GMR/acc_thickness_sweep/high_res_high_simtime/data/max_res/max_res.txt'
plot_field_max(datafilename)