# Kamil Selega zadanie 6 lista 4

import numpy as np
import matplotlib.pyplot as plt

# Możliwość włączenia rysowania wykresu
rysuj_wykres = False

# Deklaracja pierwszego równania przekształconego dla y
def pierwszeRownanie(x):
    return np.tan(x) - 1

# Deklaracja drugiego równania przekształconego dla y przy pomocy WolframAlpha
def drugieRownanie(x, n):
    y1 = 2*np.pi*n + np.arcsin(np.cos(x) / 3)
    y2 = 2*np.pi*n - np.arcsin(np.cos(x) / 3) + np.pi
    return (y1, y2)

if rysuj_wykres:
    # Deklaracja przedziału, kroku, ilości punktów, tolerancji
    x_start = 0
    x_koniec = 1.5
    ilosc = 100000
    # Wykres pierwszego równania
    x = np.linspace(x_start, x_koniec, ilosc)
    y = np.array(pierwszeRownanie(x))
    plt.plot(x, y)

    # Wykres drugiego równania
    for i in range(-1, 3):
        y1 = np.array(drugieRownanie(x, i)[0])
        y2 = np.array(drugieRownanie(x, i)[1])
        plt.plot(x, y1, "r")
        plt.plot(x, y2, "r")

    # Wyświetlenie wykresu w celu analizy
    plt.show()

    # Na wykresie widać, że w tym przedziale ten układ równań ma 5 rozwiązań.
    # Ponadto dzięki metodzie prób i błędów wiem też dla jakich wartości n
    # drugiego równania można spodziewać się rozwiązań (od 0 do 2) dla x > 0,8.

# Tolerancja i krok startowy (względnie duży)
tolerancja = 10**-7
startowy_krok = 10**-3
krok = startowy_krok

# Deklaracja pustej tablicy rozwiązań, początkowego x i pierwszych wartości y
rozwiazania = []
x = 0
n = 0
i = 0
y1 = pierwszeRownanie(x)
y2 = drugieRownanie(x, n)
nast_y1 = pierwszeRownanie(x + krok)
nast_y2 = drugieRownanie(x + krok, n)
znaleziono = False

# Pętla szukająca wszystkich (5) zaobserwowanych na wykresie rozwiązań 
while len(rozwiazania) < 5:
    # Ustalenie która z dwóch wartości drugiego równania zwracanych dla pojedynczego n jest bliższa rosnącej w przeszukiwanym przedziale funkcji pierwszej
    if y2[0] > y1:
        i = 0
    elif y2[1] > y1:
        i = 1
    else:
        n += 1
        i = 0
        y1 = pierwszeRownanie(x)
        y2 = drugieRownanie(x, n)
        nast_y1 = pierwszeRownanie(x + krok)
        nast_y2 = drugieRownanie(x + krok, n)

    # Jeśli te dwie funkcje się przecinają pomiędzy kolejnymi dużymi krokami, szukaj rozwiązania
    if (y1 - y2[i]) * (nast_y1 - nast_y2[i]) < 0:
        # Dopóki nie znaleziono rozwiązania zmniejszam krok o 0.1 co przeszukanie przedziału
        while not znaleziono:
            a = x
            # Przeszukiwanie przedziału z zadanym krokiem
            while a < x + startowy_krok:
                y1 = pierwszeRownanie(a)
                y2 = drugieRownanie(a, n)[i]
                # Jeśli różnica wartości y obydwu równań jest mniejsza od ustalonej tolerancji znaleziono rozwiązanie
                if abs(y1 - y2) < tolerancja:
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
    y2 = drugieRownanie(x, n)
    nast_y1 = pierwszeRownanie(x + krok)
    nast_y2 = drugieRownanie(x + krok, n)

# Wyświetlenie rozwiązań
print(rozwiazania)