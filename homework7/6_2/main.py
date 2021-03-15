import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

y = np.linspace(-5, 5, 50)
z = np.linspace(-5, 5, 50)
x1 = 1 - 2*y + z
x2 = (4/3)*y + 7/3
x3 = (5*y + 12 - 2*z)/8
x4 = (5*z + 7)/2
x5 = (15 + 7*z - 4*y)/11
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x1, y, z, label='parametric curve')
ax.plot(x2, y, z, label='parametric curve')
ax.plot(x3, y, z, label='parametric curve')
ax.plot(x4, y, z, label='parametric curve')
ax.plot(x5, y, z, label='parametric curve')

show()
