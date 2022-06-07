import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

cube = np.ones((3, 3, 3), dtype="bool")

colors = np.full(shape=(3, 3, 3), fill_value=["#000000"])

colors[0, 0, 0] = "#ffffff"
fig = plt.figure()

ax = plt.axes(projection="3d")
ax.set_facecolor("Grey")
ax.voxels(cube, facecolors=colors, edgecolors="w")

ax.axis("off")
plt.show()
