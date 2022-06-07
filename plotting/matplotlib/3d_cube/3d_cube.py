#! /usr/bin/env nix-shell
#! nix-shell shell-3d_cube.nix -i python

# Import libraries
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create axis
axes = [3, 3, 3]

# Create Data
data = np.ones(axes, dtype=bool)

# Control Transparency
alpha = 0.9

print("prout")

# Control colour
colors = np.empty(axes + [4], dtype=np.float32)

colors[0] = [1, 0, 0, alpha]  # red
colors[1] = [0, 1, 0, alpha]  # green
colors[2] = [0, 0, 1, alpha]  # blue
#colors[3] = [0, 1, 1, alpha]  # blue
#colors[4] = [1, 0, 1, alpha]  # blue
#colors[5] = [1, 1, 0, alpha]  # blue

# Plot figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Voxels is used to customizations of
# the sizes, positions and colors.
ax.voxels(data, facecolors=colors, edgecolors='grey')

plt.show()
