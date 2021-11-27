import numpy as np
import matplotlib.pyplot as plt

# Dziedzina i wartości
x = np.linspace(0, 1.5, 10000)
y = np.cos(x) - 3 * np.sin(np.tan(x) - 1)

# Wyświetlenie wartości x i y na wykresie
plt.plot(x, y)
plt.show()

# Jeśli sąsiadujące wartości mają przeciwne znaki, 
# oznacza to że pomiędzy nimi znajduje się miejsce zerowe
print("Przybliżone miejsca zerowe:")
for i in range(len(x)):
    if i > 0 and y[i] * y[i - 1] < 0:
        print((x[i - 1] + x[i]) / 2)

# Kamil Selega zadanie 1 lista 1