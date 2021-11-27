# Kamil Selega zadanie 1 lista 4

from scipy import optimize

# Deklaracja funkcji podanej na liście
def f(x):
    return (2*x**4 + 24*x**3 + 61*x**2 - 16*x + 1)

# Stopień wielomianu
n = 4

# Przeszukiwana dziedzina od m do -m
m = -10000

# Początek i koniec przedziału w którym szukamy pierwiastka
a = m
b = a

# Wartość o którą przesuwam granicę przedziału
D = 1
d = 0.0001

# Pierwiastki
x = []

# Przesuwam się po zadeklarowanej dziedzinie
while b < -m:
    # Jeśli różne znaki końców przedziału to szukam pierwiastka i przesuwam lewą granicę przedziału
    if f(a) * f(b) < 0:
        x.append(optimize.ridder(f, a, b))
        a = b
    # Inaczej sprawdzam czy znaleziono już wszystkie pierwiastki
    elif len(x) == 4:
        break
    # Jeśli znaleziono co najmniej jeden pierwiastek to przesuwam się małym krokiem
    if len(x) > 0:
        b += d
    # Jeśli nie znaleziono żadnego to przesuwam się dużym krokiem
    else:
        b += D

# Wyświetlenie pierwiastków
print(x)