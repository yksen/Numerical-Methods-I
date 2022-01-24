# Kamil Selega zadanie 2 lista 8

from scipy import linalg

# Dana macierz
a = linalg.hilbert(6)

# Wartości i wektory własne
eigen = linalg.eig(a)

# Wyświetlenie wyników
print(f"Wartości własne:\n{eigen[0]}")
print(f"Wektory własne:\n{eigen[1]}")
