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

# Deklaracja przedziału, kroku, ilości punktów, tolerancji
x_start = 0
x_koniec = 1.5
krok = 10**-7
ilosc = int((x_koniec - x_start) / krok)
tolerancja = 10**-6

if rysuj_wykres:
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

# Deklaracja pustej tablicy rozwiązań, początkowego x, n i pierwszych wartości y
rozwiazania = []
x = 0.8
n = 0
y1 = pierwszeRownanie(x)
y2 = drugieRownanie(x, n)

while x <= x_koniec:
    # Jeśli znaleziono wszystkie rozwiązania, przerwij pętlę
    if len(rozwiazania) == 5:
        break
    # Jeśli wartość pierwszego rów. jest większa od większej wartości drugiego przesuwam się na kolejne n
    if y1 > y2[1]:
        n += 1
    # Sprawdzenie czy moduł różnicy rozwiązań obu równań jest mniejszy od tolerancji, jeśli tak
    # dodaje rozwiązanie (x, y) do listy rozwiązań tego układu równań.
    for y in y2:
        if abs(y1 - y) < tolerancja:
            rozwiazania.append((x, y1))

    # Nowe wartości x i y
    x += krok
    y1 = pierwszeRownanie(x)
    y2 = drugieRownanie(x, n)

# Wyświetlenie rozwiązań
print(rozwiazania)