import numpy as np
import matplotlib.pyplot as plt

# A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# B = np.array([12, 2, 1])
# Определитель в матрице равен 0

A = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
B = np.array([12, 2, 1])

print(np.linalg.solve(A, B))