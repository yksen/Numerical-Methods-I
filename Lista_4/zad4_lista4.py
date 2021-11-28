# Kamil Selega zadanie 4 lista 4

import numpy as np
import matplotlib.pyplot as plt

# Możliwość włączenia rysowania wykresu
rysuj_wykres = False

# Deklaracja pierwszego równania przekształconego dla y przy pomocy WolframAlpha
def pierwszeRownanie(x):
    x = np.complex128(x)
    y = np.real((-1) ** (2/3) * np.power((-x - np.exp(-x)), 1/3))
    return y

# Deklaracja drugiego równania przekształconego dla y przy pomocy WolframAlpha
def drugieRownanie(x):
    y1 = x - np.sqrt(2*x**2 + np.tan(x))
    y2 = np.sqrt(2*x**2 + np.tan(x)) + x
    return (y1, y2)

if rysuj_wykres:
    # Ilość punktów
    n = 1000000

    # Wykres okręgu
    r = 2
    theta = np.linspace(0, 2*np.pi, n)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.plot(x, y)

    # Wykres pierwszego równania
    x = np.linspace(-r - 0.5, r + 0.5, n, dtype=np.complex128)
    y = pierwszeRownanie(x)
    plt.plot(x, y)

    # Wykres drugiego równania
    x = np.linspace(-r - 0.5, r + 0.5, n)
    y = drugieRownanie(x)
    plt.plot(x, y[0], "r")
    plt.plot(x, y[1], "r")

    # Wyświetlenie wykresu
    plt.xlim([-2.5, 2.5])
    plt.ylim([-2.5, 2.5])
    plt.show()

    # Na wykresie widoczne jest przecięcie tych dwóch równań w 3 miejscach wewnątrz okręgu
    # w przedziale mniej więcej od -1,3 do 1,3.

# Tolerancja i krok startowy (względnie duży)
tolerancja = 10**-7
startowy_krok = 10**-2
krok = startowy_krok

# Deklaracja pustej tablicy rozwiązań, początkowego x i pierwszych wartości y
rozwiazania = []
x = -1.3
y1 = pierwszeRownanie(x)
y2 = drugieRownanie(x)[0]
nast_y1 = pierwszeRownanie(x + krok)
nast_y2 = drugieRownanie(x + krok)[0]
znaleziono = False

# Pętla szukająca wszystkich (3) zaobserwowanych na wykresie rozwiązań 
while len(rozwiazania) < 3:
    # Jeśli te dwie funkcje się przecinają pomiędzy kolejnymi dużymi krokami, szukaj rozwiązania
    if (abs(y1) - abs(y2)) * (abs(nast_y1) - abs(nast_y2)) < 0:
        # Dopóki nie znaleziono rozwiązania zmniejszam krok o 0.1 co przeszukanie przedziału
        while not znaleziono:
            a = x
            # Przeszukiwanie przedziału z zadanym krokiem
            while a < x + startowy_krok:
                y1 = pierwszeRownanie(a)
                y2 = drugieRownanie(a)[0]
                # Jeśli różnica wartości y obydwu równań jest mniejsza od ustalonej tolerancji znaleziono rozwiązanie
                if abs(abs(y1) - abs(y2)) < tolerancja:
                    rozwiazania.append((a, y1))
                    znaleziono = True                    
                    break
                a += krok
            krok *= 10**-1
    # Zresetowanie wartości do przeszukiwania znalezionego przedziału
    znaleziono = False
    krok = startowy_krok
    # Aktualizacja wartości do poszukiwania odpowiedniego kandydata na przedział zawierający rozwiązanie
    x += krok
    y1 = pierwszeRownanie(x)
    y2 = drugieRownanie(x)[0]
    nast_y1 = pierwszeRownanie(x + krok)
    nast_y2 = drugieRownanie(x + krok)[0]

# Wyświetlenie rozwiązań
print(rozwiazania)
