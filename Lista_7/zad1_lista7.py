# Kamil Selega zadanie 1 lista 7

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Deklaracja równania
def f(t, y):
    return np.sin(t*y)

# Dane
y0 = [2, 2.5, 3, 3.5]
# Rozwiązania w zadanycm przedziale
rozwiazanie = solve_ivp(f, (0, 6), y0, t_eval=np.linspace(0, 6, 1000))

# Wykres rozwiązań
for i in range(len(y0)):
    plt.plot(rozwiazanie.t, rozwiazanie.y[i], label=y0[i])
plt.legend()
plt.show()