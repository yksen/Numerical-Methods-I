# Kamil Selega zadanie 2 lista 7

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Dane
A = [0.5, 0.5, 1.35]
Q = 2
omega_sr = 2/3
theta_0 = [0.01, 0.3, 0.3]
dtheta_0 = 0

# Deklaracja równania
def f(t, y, a):
    theta, dtheta = y
    return [dtheta, a*np.cos(t*omega_sr) - np.sin(theta) - 1/Q*dtheta]

# Deklaracja okna wykresu i jego podwykresów
okno, osie = plt.subplots(2, 3)

# Przedział czasu
t = np.linspace(0, 50, 1000)

# Rozwiązanie dla każdego zestawu warunków początkowych i naniesienie ich na wykres wraz z opisem osi
for i in range(len(theta_0)):
    rozw = solve_ivp(f, y0=[theta_0[i], dtheta_0], t_span=(t[0], t[-1]), t_eval=t, args=[A[i]], method="LSODA")
    osie[0, i].plot(rozw.t, rozw.y[1])
    osie[0, i].set_xlabel("t")
    osie[0, i].set_ylabel("theta")
    osie[1, i].plot(rozw.y[1], rozw.y[0])
    osie[1, i].set_xlabel("theta")
    osie[1, i].set_ylabel("dtheta")

# Wyświetlenie wykresu
plt.show()

