import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.lines import Line2D
from matplotlib.colorbar import ColorbarBase

# Create some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(2 * x)
y4 = np.cos(2 * x)

# Create a colormap
cmap = cm.viridis

# Plot the line plots with different colors
fig, ax = plt.subplots()
lines = []
lines.append(ax.plot(x, y1, label='Line 1')[0])
lines.append(ax.plot(x, y2, label='Line 2')[0])
lines.append(ax.plot(x, y3, label='Line 3')[0])
lines.append(ax.plot(x, y4, label='Line 4')[0])

# Create a ScalarMappable object
norm = plt.Normalize(0, len(lines))
scalar_mappable = cm.ScalarMappable(cmap=cmap, norm=norm)
scalar_mappable.set_array([])  # You need to set an array for the scalar mappable

# Add colorbar
cbar = plt.colorbar(scalar_mappable, ax=ax, orientation='vertical', fraction=0.02, pad=0.1)
cbar.set_label('Colorbar Label')

# Customize color for each line using the colormap
for i, line in enumerate(lines):
    line.set_color(cmap(norm(i)))

# Add legend
ax.legend()

plt.savefig('testingtesting.png')
