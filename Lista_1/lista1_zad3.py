import numpy as np

# Deklaracja macierzy
a = np.array([[4, -2, 1], [-2, 4, -2], [1, -2, 4]])
b = np.array([[4, 2, 0], [2, 5, 2], [0, 2, 4]])
w = np.array([[1], [-2], [3]])

# Wyniki mnożenia
print("AB\n", np.matmul(a, b))
print("Aw\n", np.matmul(a, w))
print("B(Aw)\n", np.matmul(b, np.matmul(a, w)))

# Wyznaczniki macierzy
print("det(A)\n", np.linalg.det(a))
print("det(B)\n", np.linalg.det(b))

# Macierze odwrotne
print("inv(A)\n", np.linalg.inv(a))
print("inv(B)\n", np.linalg.inv(b))

# Kamil Selega zadanie 3 lista 1