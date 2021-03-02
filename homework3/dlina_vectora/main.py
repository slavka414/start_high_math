#

import numpy as np

x = int(input('Введи координату Х вектора:   '))
y = int(input('Введи координату Y вектора:   '))
z = int(input('Введи координату Z вектора:   '))

long = np.sqrt(x ** 2 + y ** 2 + z ** 2)

print(long)