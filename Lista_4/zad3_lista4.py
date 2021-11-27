# Kamil Selega zadanie 3 lista 4

import numpy as np

# Dane
u = 2510
Mo = 2.8 * 10**6
m = 13.3 * 10**3
g = 9.81

# Prędkość dźwięku
Vd = 335

# Czas i krok
t = 0
dt = 0.001

# Prędkość rakiety
def v(t):
    return u * np.log(Mo/(Mo - m * t)) - g * t

# Znalezienie czasu w którym rakieta osiąga prędkość dźwięku
while v(t) < Vd:
    t += dt

print(t, v(t))