# Kamil Selega zadanie 2 lista 4

def pierwiastekPiategoStopnia(x0):
    tolerancja = 10**-9
    poprzedni = x0
    # Liczenie kolejnego przybliżenia pierwiastka metodą Newtona
    aktualny = (1/5) * (4*x0 + (x0/(x0**4)))
    # Liczenie kolejnych przybliżeń do momentu gdy różnica dwóch kolejnych jest mniejsza od zdefiniowanej
    while abs(aktualny - poprzedni) > tolerancja:
        poprzedni = aktualny
        aktualny = (1/5) * (4*aktualny + (x0/(aktualny**4)))
    return aktualny

# Pierwiastek piątego stopnia pierwszysch 100 liczb naturalnych
for i in range(1, 101):
    print(i, "\t", pierwiastekPiategoStopnia(i), "\t", i**(1/5))