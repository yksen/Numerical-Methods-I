# Kamil Selega zadanie 4 lista 7

from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import newton

# Dane
a = 0
b = np.pi
y_a = 0
y_b = 0

# Definicja równania różniczkowego
def f(t, y):
    return [y[1], -np.sin(y[0]) - 1]

# Funkcja sprawdzająca różnicę wartości dla testowego parametru "u" dla drugiego brzegu.
def g(u):
    roz = solve_ivp(f, (a, b), [y_a, u], t_eval=np.linspace(a, b, 1000))
    return roz.y[0, -1] - y_b

# Wykres różnic wartości równania dla różnych wartości parametru "u" dla drugiego brzegu.
u = np.arange(0, 4, 0.1)
vg = np.vectorize(g)
plt.plot(u, vg(u), label="g(u)")
plt.axhline(y=0, color="black", label="y = 0")
plt.xlabel("u")
plt.ylabel("g")
plt.legend()
plt.show()
# Z wykresu jestem w stanie odczytać, że nasza druga wartość brzegowa wynosi około 2,8.

# Dzięki temu znalezienie wartości początkowej y"(0) sprowadza się do znalezienia
# pierwiastka funkcji g. Użyję w tym celu metody Newtona z modułu optimize.
u0 = 2.5
u = newton(g, u0)
roz = solve_ivp(f, (a, b), [y_a, u], t_eval=np.linspace(a, b, 1000))
plt.plot(roz.t, roz.y[0], label="y(t)")
plt.plot(roz.t, roz.y[1], label="y'(t)")
plt.plot([a, b], [y_a, y_b], "o", label="Warunki brzegowe")
plt.legend()
plt.show()
