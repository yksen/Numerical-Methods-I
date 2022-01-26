# Kamil Selega zadanie 3 lista 8

import numpy as np
from scipy.sparse import dia_matrix
from scipy.sparse.linalg import eigsh

# Dane
n = 10, 100

for i in n:
    # Macierz rozmiaru n x n wypełniona jedynkami
    macierz = np.ones(i)
    # Wartości na diagonalach macierzy i ich przesunięcia względem głównej diagonali
    wartosci = [-macierz, 2 * macierz, -macierz]
    przesuniecia = [-1, 0, 1]
    # Utworzenie macierzy o wartościach takich jak w poleceniu na odpowiednich diagonalach
    macierz = dia_matrix((wartosci, przesuniecia), shape=(i, i)).toarray()
    # Znalezienie trzech najmniejszych algebraicznie wartości własnych naszej macierzy i ich wektorów własnych
    eigen = eigsh(macierz, 3, which="SA")

    # Wyświetlenie wyników
    print(f"n = {i}")
    print(macierz)
    print(f"Wartości własne:\n{eigen[0]}")
    print(f"Wektory własne:\n{eigen[1]}\n")