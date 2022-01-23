# Kamil Selega zadanie 1 lista 8

import numpy as np
from scipy import linalg

# Dana macierz
a = np.array([[-1, -4, 1], [-1, -2, -5], [5, 4, 3]])

# Wartości i wektory własne
eigen = linalg.eig(a)

print(f"Wartości własne:\n{eigen[0]}")

print(f"Wektory własne:")
for i in eigen[1]:
    print([f"{j:.3f}" for j in i])
