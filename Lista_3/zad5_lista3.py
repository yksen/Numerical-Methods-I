# Kamil Selega zadanie 5 lista 3

import numpy as np

def eliminacja_Gaussa(a: np.ndarray, b: np.ndarray):
    # Rozmiar macierzy a powiększony o jedną kolumnę dla macierzy b
    size = (a.shape[0], a.shape[1] + 1)

    # Złączenie macierzy a i b w jedną
    m = np.zeros(size)
    for i in range(size[0]):
        for j in range(size[1]):
            if j < size[1] - 1:
                m[i, j] = a[i, j]
            else:
                m[i, j] = b[i, j - size[1]]

    # Doprowadzenie macierzy m do macierzy dolnotrójkątnej
    for k in range(size[0]):
        # Znalezienie rzędu z największym współczynnikiem
        i_max = k
        v_max = m[i_max, k]
        for i in range(k + 1, size[0]):
            if abs(m[i, k] > v_max):
                v_max = m[i, k]
                i_max = i

        # Zamiana rzędu z największym współczynnikiem z aktualnym
        if i_max != k:
            for i in range(size[1]):
                tmp = m[k, i]
                m[k, i] = m[i_max, i]
                m[i_max, i] = tmp

        for i in range(k + 1, size[0]):
            # Obliczenie wartości stosunku współczynnika z "niższego" rzędu i aktualnego
            f = m[i, k] / m[k, k]
            # Odjęcie iloczynów stosunku f i współczynnika z odpowiadającego rzędu
            for j in range(k + 1, size[1]):
                m[i, j] -= m[k, j] * f
            # Umieszczenie zera w macierzy w miejscu wyzerowanej wartości
            m[i, k] = 0

    # Obliczenie wartości macierzy x
    x = np.zeros(b.shape)
    for i in range(size[0] - 1, -1, -1):
        # Wyraz wolny
        x[i] = m[i, size[0]]
        # Odjęcie iloczynów już obliczonych x-ów i ich współczynników
        for j in range(i + 1, size[0]):
            x[i] -= m[i, j] * x[j]
        # Ostateczny wynik jako iloraz różnicy iloczynów i współczynnika przy obliczanej zmiennej
        x[i] = x[i] / m[i, i]

    # Wyświetl macierz x będącą rozwiązaniem równania Ax = b
    print(x)

# Zadanie 1
a = np.array([[-1, 1, -4], [2, 2, 0], [3, 3, 2]])
b = np.array([[0], [1], [0.5]])
print("Zadanie 1")
eliminacja_Gaussa(a, b)

# Zadanie 2
l = np.array([[1, 0, 0], [3/2, 1, 0], [1/2, 11/13, 1]])
u = np.array([[2, -3, -1], [0, 13/2, -7/2], [0, 0, 32/13]])
a = np.matmul(l, u)
b = np.array([[1], [-1], [2]])
print("Zadanie 2")
eliminacja_Gaussa(a, b)

# Zadanie 3
a = np.array([[0, 0, 2, 1, 2], [0, 1, 0, 2, -1], [1, 2, 0, -2, 0], [0, 0, 0, -1, 1], [0, 1, -1, 1, -1]])
b = np.array([[1], [1], [-4], [-2], [-1]])
print("Zadanie 3")
eliminacja_Gaussa(a, b)