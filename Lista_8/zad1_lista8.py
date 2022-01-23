# Kamil Selega zadanie 1 lista 8

from contextlib import suppress
import numpy as np
from scipy import linalg

# Dana macierz
a = np.array([[-1, -4, 1], [-1, -2, -5], [5, 4, 3]])

# Wartości i wektory własne
eigen = linalg.eig(a)

# Wyświetlenie sformatowanych wyników. 
# Warto dodać, że wektory własne odczytywane są w pionie, a nie w poziomie.
np.set_printoptions(3, suppress=True)
print(f"Wartości własne:\n{eigen[0]}")
print(f"Wektory własne:\n{eigen[1]}")