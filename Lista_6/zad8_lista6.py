# Kamil Selega zadanie 8 lista 6

import numpy as np
from scipy.integrate import dblquad

# Deklaracja równania
def f(x, y):
    return np.sin(np.pi * x) * np.sin(np.pi * (y - x))

# Podwójna całka na zadanych przedziałach x: 0..1, y: 0..x
print(dblquad(f, 0, 1, lambda x: x, lambda x: 0))