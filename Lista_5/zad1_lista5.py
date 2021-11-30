# Kamil Selega zadanie 1 lista 5

import numpy as np
import matplotlib.pyplot as plt

# Dane
h = np.array([0, 3, 6])
rho = np.array([1.225, 0.905, 0.652])
plt.plot(h, rho)

# Dopasowanie współczynników wielomianu stopnia drugiego do danych
a = np.polyfit(h, rho, 2)
x = np.linspace(h[0] - 1, h[-1] + 1, 100)
y = a[0] * x**2 + a[1] * x**1 + a[2] * x**0
plt.plot(x, y)

plt.show()