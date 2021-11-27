# Kamil Selega zadanie 6 lista 3

import numpy as np

# Funkcja zwracająca macierz Hilberta dla danego rozmiaru n
def macierz_Hilberta(n):
    m = np.empty((n, n))
    for i in range(n):
        for k in range(n):
            m[i][k] = 1 / (i + k + 1)
    return m

# Deklaracja macierzy
H5 = macierz_Hilberta(5)
H10 = macierz_Hilberta(10)
H20 = macierz_Hilberta(20)

# Normy i wskaźniki uwarunkowania macierzy
print("n=5\t" + str(np.linalg.norm(H5)), np.linalg.cond(H5), sep="\t")
print("n=10\t" + str(np.linalg.norm(H10)), np.linalg.cond(H10), sep="\t")
print("n=20\t" + str(np.linalg.norm(H20)), np.linalg.cond(H20), sep="\t")