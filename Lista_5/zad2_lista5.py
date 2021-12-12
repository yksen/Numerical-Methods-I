# Kamil Selega zadanie 2 lista 5

import numpy as np
from scipy.interpolate import CubicSpline

# Dane
x = np.arange(1, 3.25, 0.25)
y = np.array([-0.5403, -0.0104, 0.9423, 1.7445, 1.3073, -0.7718, -2.4986, -0.7903, 2.7334])

# Interpolacja funkcjami sklejanymi
cs = CubicSpline(x, y)

# Wartość y'(2.1)
print("y'(2.1) = ", cs(2.1, 1))

# Pierwiastki y(x)
print(cs.roots())