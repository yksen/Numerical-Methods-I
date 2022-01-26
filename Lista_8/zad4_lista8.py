# Kamil Selega zadanie 4 lista 8

import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
import matplotlib.pyplot as plt

# Dane
lamb = 0.2
M = 100, 1000
a = 4.6

for m in M:
    # Siatka równoodległych punktów
    i = np.arange(0, m, 1)
    h = (2*a)/m
    x = -a + i*h
    # Wartości
    g = -1/(2*h**2)
    d = 1/h**2 + x**2/2 + lamb*x**4

    # Wartości na odpowiednich diagonalach
    wartosci = [g, d, g]
    przesuniecia = [-1, 0, 1]
    # Stworzenie odpowiedniej macierzy
    macierz = diags(wartosci, przesuniecia, (m, m)).toarray()
    # Znalezienie czterech najmniejszych algebraicznie wartości własnych naszej macierzy i ich wektorów własnych
    eigen = eigsh(macierz, 4, which="SA")

    # Wyświetlenie wyników
    print(f"m = {m}")
    # print(macierz)
    print(f"Wartości własne:\n{eigen[0]}")
    print(f"Wektory własne:\n{eigen[1]}\n")
    print(eigen[1].T)
    # Wykresy funkcji falowych dla czterech najmniejszych wartości własnych dla obydwu wartości m
    okno, wykr = plt.subplots(2, 2)
    okno.suptitle(f"m = {m}")
    for j in range(len(eigen[1].T)):
        wykr[j%2, int(j>1)].plot(np.linspace(-1, 1, len(eigen[1].T[j])), eigen[1].T[j])
        wykr[j%2, int(j>1)].set_title(f"Energia = {eigen[0][j]}")

plt.show()