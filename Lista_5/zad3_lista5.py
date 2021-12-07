# Kamil Selega zadanie 3 lista 5

import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Dane
Re = np.log10(np.array([0.2, 2, 20, 200, 2000, 20000]))
cp = np.log10(np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433]))

# Interpolacja
xs = np.arange(Re[0], Re[-1], 0.01)
cs = CubicSpline(Re, cp)

# Wartości dla Re = 5.5 i Re = 5000
print("Re = 5.5, cp = ", cs(np.log10(5.5)), "\nRe = 5000, cp = ", cs(np.log10(5000)))

# Wykres
plt.scatter(Re, cp)
plt.plot(xs, cs(xs))
plt.show()