from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Definicja równania różniczkowego
def f(x, y):
    return 2*x - y**2 - 1

# Definicja funkcji znajdującej pierwiastki
def pierwiastek(x, y):
    return y

# Dane
x = (0, 4)
y0 = [.2]

# Rozwiązanie
roz = solve_ivp(f, x, y0, events=pierwiastek, rtol=1e-10, atol=1e-12)

# Znalezione pierwiastki
print(f"Pierwiastki znalezione w badanym przedziale to: {roz.t_events[0]}")

# Wykres rozwiązań
plt.axhline(0, color="red", linestyle="--")
plt.plot(roz.t, roz.y[0], label = "y(x)")
plt.legend()
plt.show()