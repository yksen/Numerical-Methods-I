# Kamil Selega zadanie 7 lista 6

import numpy as np
from scipy.integrate import quadrature

# Deklaracja równania
def f(x):
    return (np.cos(x) - np.exp(x)) / np.sin(x)

# Całka tego równania na całym przedziale.
# Niestety funkcja na tym przedziale nie zwraca z jakiegość powodu dokładności.
print(quadrature(f, -1, 1))

# Całki na dwóch osobnych przedziałach po lewej i prawej stronie od punktu x=0
sum1 = quadrature(f, -1, 0)
sum2 = quadrature(f, 0, 1)
# Suma wartości tych całek i suma ich dwóch dokładności 
print((sum1[0] + sum2[0], sum1[1] + sum2[1]))

# Zauważyłem, że oba te wyniki zaczynają się rozbiegać dopiero na jedenastym miejscu
# po przecinku co najprawdopodobniej świadczy o dokładności do dziesiątego miejsca.
