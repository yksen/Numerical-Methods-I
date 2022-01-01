# Kamil Selega zadanie 5 lista 6

import numpy as np
from scipy.integrate import simpson

def h(theta_0):
    theta = np.linspace(0, np.pi/2, 1000)
    y = theta / (np.sqrt(1 - np.sin(theta_0 / 2)**2 * np.sin(theta)**2))
    return simpson(y, theta)

# Wartość porównawcza
print("h(0°) =", np.pi/2)

# Obliczone wartości dla wskazanych kątów
for theta in np.arange(15, 60, 15):
    print(f"h({theta}°) =", h(np.deg2rad(theta)))