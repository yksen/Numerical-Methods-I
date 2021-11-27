import numpy as np

# Funkcja zwracająca macierz Hilberta dla danego rozmiaru n
def macierz_Hilberta(n):
    m = np.empty((n, n))
    for i in range(n):
        for k in range(n):
            m[i][k] = 1 / (i + k + 1)
    return m

# Zmiana wyświetlanej ilości miejsc po przecinku w celu czytelniejszego rezultatu
np.set_printoptions(precision=3)

# Wyświetlenie macierzy Hilberta
print("Macierz Hilberta dla:")
print("n = 4\n", macierz_Hilberta(4))
print("n = 8\n", macierz_Hilberta(8))

# Wyświetlenie macierzy odwrotnych do macierzy Hilberta
print("\nMacierze Hilberta odwrotne dla:")
print("n = 4\n", np.linalg.inv(macierz_Hilberta(4)))
print("n = 8\n", np.linalg.inv(macierz_Hilberta(8)))

# Wyznaczniki macierzy Hilberta
print("\nWyznaczniki macierzy Hilberta dla n od 5 do 20:")
for i in range(5, 21):
    print("n =", i, "\t", np.linalg.det(macierz_Hilberta(i)))

# Kamil Selega zadanie 4 lista 1