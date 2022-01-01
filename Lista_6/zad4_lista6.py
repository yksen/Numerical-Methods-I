# Kamil Selega zadanie 4 lista 6

import numpy as np
from scipy.integrate import simpson

def f(n):
    x = np.linspace(-1, 1, n)
    y = np.cos(2*np.arccos(x))
    return simpson(y, x)

# Metoda Simpsona dla trzech węzłów
print(f(3))

# Metoda Simpsona dla pięciu węzłów
print(f(5))

# Metoda Simpsona dla siedmiu węzłów
print(f(7))