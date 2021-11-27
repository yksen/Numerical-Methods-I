# Kamil Selega zadanie 7 lista 4

import numpy as np

# Deklaracja wielomianu podanego na liście
w = np.poly([1, 5 + 1j, -(8 - 5j), (30 - 14j), -84])

# Pierwiastki wielomianu
x = np.roots(w)

# Wyświetlenie pierwiastków
print(x)