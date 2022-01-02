# Kamil Selega zadanie 6 lista 6

import numpy as np
from scipy.integrate import fixed_quad

# Deklaracja równania
def f(x):
    return np.log(x) / (x**2 - 2*x + 2)

# Całki liczone metodą Gaussa-Legendre'a dla dwóch i czterech węzłów
print(fixed_quad(f, 1, np.pi, n=2))
print(fixed_quad(f, 1, np.pi, n=4))