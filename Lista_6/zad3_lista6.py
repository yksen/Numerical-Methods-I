# Kamil Selega zadanie 3 lista 6

import numpy as np
from scipy.interpolate import lagrange

# Dane
x = np.array([-2.2, -0.3, 0.8, 1.9])
y = np.array([-15.18, 10.962, 1.92, -2.04])

# Interpolacja wielomianowa
p = lagrange(x, y)

# Wartości pierwszej i drugiej pochodnej dla x=0 otrzymanego wielomianu
print("f'(0) = ", np.polyval(np.polyder(p, 1), 0))
print("f''(0) = ", np.polyval(np.polyder(p, 2), 0))