import numpy as np
import matplotlib.pyplot as plt

from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange(-50, 50, 1)
Y = np.arange(-50, 50, 1)
X, Y = np.meshgrid(X, Y)
Z2 = X + 30
Z1 = X
ax.plot_surface(X, Y, Z1)
ax.plot_surface(X, Y, Z2)
show()
