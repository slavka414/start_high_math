#

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 7, 300)
plt.plot(x, np.cos(2 * x))
plt.plot(x, np.cos(x))
plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
plt.show()