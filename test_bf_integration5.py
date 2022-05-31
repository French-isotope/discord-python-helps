import numpy as np
import matplotlib.colors as colors
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

samples = np.random.randint(91,size=(5000,2))

F = np.zeros([91,91])
for s in samples:
    F[s[0],s[1]] += 1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x_data, y_data = np.meshgrid( np.arange(F.shape[1]),
                              np.arange(F.shape[0]) )
x_data = x_data.flatten()
y_data = y_data.flatten()
z_data = F.flatten()

dz = F
offset = dz + np.abs(dz.min())
fracs = offset.astype(float)/offset.max()
norm = colors.Normalize(fracs.min(), fracs.max())
colors = cm.jet(norm(fracs))

ax.bar3d(x_data,y_data,np.zeros(len(z_data)),1,1,z_data,color=colors.reshape(-1,4) )
plt.show()