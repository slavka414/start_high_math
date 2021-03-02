import numpy as np
from matplotlib import pyplot as plt

xmin = -20
xmax = 20
dx = 0.1

xlist = np.around(np.arange(xmin, xmax, dx), decimals=1)

ylist = 1 / xlist

plt.plot(xlist, ylist)
plt.show()
