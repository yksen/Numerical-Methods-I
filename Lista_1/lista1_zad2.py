import matplotlib.pyplot as plt

# Ilość elementów, wyraz początkowy
n = range(100)
x = [0.1]

# Kolejne elementy ciągu
for i in n:
    x.append(3.5 * x[-1] * (1 - x[-1]))

# Usunięcie nadliczbowego elementu w celu wyświetlenia wykresu
x.pop(-1)

# Stworzenie wykresu typu scatter
plt.scatter(n, x)
plt.show()

# Kamil Selega zadanie 2 lista 1