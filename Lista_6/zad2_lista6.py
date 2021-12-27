# Kamil Selega zadanie 2 lista 6

import numpy as np
from scipy.interpolate import CubicSpline

# Dane
x = np.linspace(0, 0.4, 5)
y = np.array([0.0, 0.078348, 0.13891, 0.192916, 0.244981])

# Interpolacja funkcjami sklejanymi
cs = CubicSpline(x, y)

# Wartość f'(0.2)
print("f'(0.2) = ", cs(0.2, 1))