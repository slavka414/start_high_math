import numpy as np
import math

p = int(input('Введите полярный радиус:  '))
f = int(input('Введите полярный угол:  '))

print(f'Точка имеет декартовые координаты ({round(p * np.cos(f*np.pi/180), 2)}, {round(p * np.sin(f*np.pi/180), 2)})')
# print(round(np.sin(f*np.pi/180), 2))
# print(round(np.cos(f*np.pi/180), 2))
