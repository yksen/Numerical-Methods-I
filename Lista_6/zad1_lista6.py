# Kamil Selega zadanie 1 lista 6

import numpy as np
from scipy.misc import central_diff_weights as cdw

def f(x):
    return np.log(np.complex(np.tanh(x / (x**2 + 1))))

# Wartość pochodnej dla wartości x
x = 0.2
# Ilość punktów dla metody różnicy centralnej
ilosc_punktow = 5

# Wagi i wartości pierwszej pochodnej
nr_pochodnej = 1
wagi = cdw(ilosc_punktow, nr_pochodnej) 
krok = 1e-9
wartosci = [f(x + (i - ilosc_punktow/2) * krok) for i in range(ilosc_punktow)]
print(f"f'({x}) = ", sum(w * v for (w, v) in zip(wagi, wartosci))/(krok**nr_pochodnej))

# Wagi i wartości drugiej pochodnej
nr_pochodnej = 2
wagi = cdw(ilosc_punktow, nr_pochodnej)  
krok = 1e-5
wartosci = [f(x + (i - ilosc_punktow/2) * krok) for i in range(ilosc_punktow)]
print(f"f''({x}) = ", sum(w * v for (w, v) in zip(wagi, wartosci))/(krok**nr_pochodnej))

# Wagi i wartości trzeciej pochodnej
nr_pochodnej = 3
wagi = cdw(ilosc_punktow, nr_pochodnej)
krok = 1e-5  
wartosci = [f(x + (i - ilosc_punktow/2) * krok) for i in range(ilosc_punktow)]
print(f"f'''({x}) = ", sum(w * v for (w, v) in zip(wagi, wartosci))/(krok**nr_pochodnej))

# Wartości liczone tak jak w przykładzie znajdującym się w dokumentacji SciPy.
# Wartości kroku zostały znalezione metodą prób i błędów uprzednio sprawdzając 
# dokładne wyniki przy pomocy WolframAlpha.
