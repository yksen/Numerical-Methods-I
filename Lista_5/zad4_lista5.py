# Kamil Selega zadanie 4 lista 5

import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

# Dane w skali podwójnie logarytmicznej
Re = np.array([0.2, 2, 20, 200, 2000, 20000])
cp = np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433])

# Interpolacja wielomianowa (Lagrange'a)
xs = np.arange(Re[0], Re[-1], 0.01)
poly = lagrange(np.log10(Re), np.log10(cp))

# Wartości dla Re = 5, Re = 50 i Re = 5000
print("Re = 5, \tcp =", 10**poly(np.log10(5)),"\nRe = 50,\tcp =", 10**poly(np.log10(50)) , "\nRe = 5000,\tcp =", 10**poly(np.log10(5000)))

# Wykres
plt.scatter(Re, cp)
plt.loglog(xs, 10**poly(np.log10(xs)))
plt.show()