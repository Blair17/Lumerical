import numpy as np
import os
import matplotlib.pyplot as plt

def plot_field_max(filepath):
    
    root = os.getcwd()

    datafilepath = os.path.join(
        root,
        filepath)
    thickness, field_max = np.genfromtxt(
        fname=datafilepath,
        delimiter=",",
        skip_header=0,
        unpack=True)
    
    T_array = np.linspace(0,200,20)
    colors = len(T_array)
    cmap = plt.cm.rainbow(np.linspace(0,1,colors))

    # for (t, f, c) in zip(thickness, field_max, range(colors)):
    fig, ax = plt.subplots(figsize=[10,5])
    ax.scatter(thickness, field_max, color=cmap, s=200)
    ax.plot(thickness, field_max, '--', lw=2, color='k', alpha=0.5)
    ax.set_xlabel('Pedestal Thickness [nm]', fontsize=18, fontweight='bold')
    ax.set_ylabel('Field max [V/m]', fontsize=18, fontweight='bold')
    ax.tick_params(axis='both', labelsize=18)
    ax.set_title('Pedestal Thickness vs Field max', fontsize=20)

    plt.tight_layout()
    plt.savefig('2D_hole_pedestal_thickness_inv/Field_max_plot.png')

datafilename = '/Volumes/Sam/Lumerical/2D_GMR/test/data/field_plots/field_plots.txt'
plot_field_max(datafilename)