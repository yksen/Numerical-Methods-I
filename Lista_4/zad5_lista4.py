# Kamil Selega zadanie 5 lista 4

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Dane
h_koszykarza = 2
h_kosza = 3
alfa_docelowe = 45
d = 10
g = 9.81

# W celu uwzględnienia kąta pod którym piłka musi wpaść do kosza, potraktuje to zadanie tak
# jakby rzut był wykonywany z pozycji kosza w stronę koszykarza z kątem początkowym 45 stopni,
# co odzwierciedla poniższy układ równań.
def uklad(zmienne):
    (v0, t) = zmienne
    return [
        v0 * np.cos(np.deg2rad(alfa_docelowe)) * t - d,
        h_kosza + v0 * np.sin(np.deg2rad(alfa_docelowe)) * t - (g * t**2)/2 - h_koszykarza
    ]

# Znalezienie pierwiastków układu równań przy użyciu scipy.optimize.fsolve
pierwiastki = fsolve(uklad, [10, 5])

# Wartości początkowe dla rzutu z perspektywy koszykarza
(v0, t) = pierwiastki
# Składowe prędkości
v0x = v0 * np.cos(np.deg2rad(alfa_docelowe))
v0y = v0 * np.sin(np.deg2rad(alfa_docelowe)) - g*t
# Prędkość z twierdzenia Pitagorasa składowych
v = np.sqrt(v0x**2 + v0y**2)
# Kąt pod którym koszykarz musi wyrzucić piłkę
alfa = np.degrees(np.arctan(v0y / -v0x))
print("v0 = ", v)
print("alfa = ", alfa)

# Wykres rzutu ukośnego
x = np.linspace(0, t, 1000)
plt.plot(v0 * np.cos(np.deg2rad(alfa_docelowe)) * x, h_kosza + v0 * np.sin(np.deg2rad(alfa_docelowe)) * x - (g * x**2)/2, "r")
plt.scatter([0, d], [h_kosza, h_koszykarza])
plt.text(0, h_kosza - 1/2, "Kosz")
plt.text(d, h_koszykarza - 1/2, "Koszykarz")
plt.axis("equal")
plt.show()