# Kamil Selega zadanie 3 lista 7

from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Dane
cw = 0.35
rho = 1.2
g = 9.80665

m = 1
r = [0.2, 0.4, 0.5]
v0 = [30, 35, 50]
alfa = np.radians([35, 35, 65])
A = np.pi*np.power(r, 2)
Fd = -1/2 * cw * rho * A

# Definicja równania różniczkowego
def f(t, u, i):
    x, vx, y, vy = u
    v = np.sqrt(vx**2 + vy**2)
    ax = Fd[i]/m * v * vx
    ay = Fd[i]/m * v * vy - g
    return [vx, ax, vy, ay]

# Deklaracja okna wykresu i jego podwykresów
okno, wykr = plt.subplots(1, 2)

for i in range(len(r)):
    # Podpunkt a)
    czas_lotu = 2 * v0[i] * np.sin(alfa[i]) / g
    # Zasięg
    x_max = v0[i] * czas_lotu * np.cos(alfa[i])
    t = np.linspace(0, czas_lotu, 1000)
    # Położenia w zależności od czasu
    x = np.linspace(0, x_max, 1000)
    y = v0[i] * t * np.sin(alfa[i]) - g*t**2 / 2
    wykr[0].plot(x, y, label=f"α={np.degrees(alfa[i])}, v0={v0[i]}")

    # Podpunkt b)
    # Prędkości początkowe
    v0x = v0[i] * np.cos(alfa[i])
    v0y = v0[i] * np.sin(alfa[i])
    # Rozwiązanie dla punktu startowego (0, 0) i prędkości v0x, v0y
    roz = solve_ivp(f, (0, 10), [0, v0x, 0, v0y], t_eval=np.linspace(0, 10, 1000), args=[i])
    # Znalezienie ostatniego indeksu dodatniego igreka, aby nanieść poprawnie na wykres tor lotu
    ostatni_indeks = np.where(roz.y[2] >= 0)[0][-1]
    wykr[1].plot(roz.y[0][0:ostatni_indeks], roz.y[2][0:ostatni_indeks], label=f"α={np.degrees(alfa[i])}, v0={v0[i]}, r={r[i]}")

# Wyświetlenie wykresu
wykr[0].set_xlabel("x")
wykr[0].set_ylabel("y")
wykr[0].legend()
wykr[1].set_xlabel("x")
wykr[1].set_ylabel("y")
wykr[1].legend()
plt.show()
