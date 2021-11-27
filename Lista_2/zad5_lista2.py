# Kamil Selega zadanie 5 lista 2

import numpy as np

e = np.exp(1)

def f(n):
    if n == 1:
        return 1
    else:
        return e - n * f(n - 1)

for n in range(2, 21):
    print(n, f(n), sep="\t")

# Wyniki od n=17 wzwyż są niepoprawne, kolejne wyniki powinny zbliżać się do zera, 
# natomiast tu obserwujemy ogromne rozbieżności i zmiany znaków.
# Jest to skutkiem niedokładności użytego związku rekurencyjnego.