# Kamil Selega zadanie 5 lista 5

import numpy as np
import matplotlib.pyplot as plt

# Dane
x = np.array([1, 2.5, 3.5, 4, 1.1, 1.8, 2.2, 3.7])
y = np.array([6.008, 15.722, 27.13, 33.772, 5.257, 9.549, 11.098, 28.828])
# Posortowanie danych
indeksy = np.argsort(x)
x = x[indeksy]
y = y[indeksy]
# Naniesienie danych na wykres
plt.scatter(x, y)

# Dopasowanie współczynników wielomianu stopnia pierwszego do danych
a1 = np.polyfit(x, y, 1)
# Dopasowanie współczynników wielomianu stopnia drugiego do danych
a2 = np.polyfit(x, y, 2)

# Naniesienie prostej i funkcji kwadratowej na wykres
xw = np.linspace(x[0] - 1, x[-1] + 1, 100)
y1 = a1[0] * xw**1 + a1[1] * xw**0
plt.plot(xw, y1, "orange")
y2 = a2[0] * xw**2 + a2[1] * xw**1 + a2[2] * xw**0
plt.plot(xw, y2, "red")

# Wyświetlenie wykresu
plt.show()

# Na podstawie wykresu, wnioskuję, że lepiej dopasowana do tego zestawu danych jest funkcja kwadratowa.