# Kamil Selega zadanie 4 lista 3

import numpy as np

# Współrzędne podanych punktów
x = np.array([0, 1, 3, 5, 6])
y = np.array([-1, 1, 3, 2, -2])

# Dopasowanie współczynników do punktów przy użyciu funkcji polyfit z modułu numpy
wspolczynniki = np.polynomial.polynomial.polyfit(x, y, 4)

print(wspolczynniki)