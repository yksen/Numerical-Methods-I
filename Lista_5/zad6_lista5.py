# Kamil Selega zadanie 6 lista 5

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splrep, splev

# Dane
h = np.arange(0, 9.150, 1.525)
rho = np.array([1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741])

# Dopasowanie funkcji kwadratowej metoa najmniejszch kwadratów
spl = splrep(h, rho)

# Wartość rho(10.5)
print(splev(10.5, spl))