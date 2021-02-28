import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x1 = int(input('Введите координату х первой точки: '))
y1 = int(input('Введите координату y первой точки: '))
x2 = int(input('Введите координату х второй точки: '))
y2 = int(input('Введите координату y второй точки: '))

plt.plot([x1, x2], [y1, y2])
plt.show()

