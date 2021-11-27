# Kamil Selega zadanie 4 lista 4

import numpy as np
import matplotlib.pyplot as plt

# Promień okręgu
r = 2

# Współrzędne n punktów oddalonych o promień r od punktu (0, 0)
n = 1000
theta = np.linspace(0, 2*np.pi, n)
x = r * np.cos(theta)
y = r * np.sin(theta)

# Naniesienie okręgu na wykres
plt.plot(x, y)

# Pierwsza funkcja w dziedzinie okolicy okręgu
x = np.linspace(-r - 0.5, r + 0.5, n, dtype=np.complex128)
y = (-1) ** (2/3) * np.power((-x - np.exp(-x)), 1/3)

# Naniesienie pierwszej funkcji na wykres
plt.plot(x, y)

# Druga funkcja
y = x - np.sqrt(2*x**2 + np.tan(x))
plt.plot(x, y)
y = np.sqrt(2*x**2 + np.tan(x)) + x
plt.plot(x, y)

# Wyrównanie osi i wyświetlenie okna
plt.axis('equal')
plt.show()
