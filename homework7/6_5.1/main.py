import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

y = np.linspace(-5, 5, 50)
z = np.linspace(-5, 5, 50)
x1 = 1 - 2*y + z
x3 = (5*y + 12 - 2*z)/8

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x1, y, z, label='parametric curve')
ax.plot(x3, y, z, label='parametric curve')

show()