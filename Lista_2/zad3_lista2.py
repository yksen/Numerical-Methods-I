# Kamil Selega zadanie 3 lista 2

for n in range(2, 26, 2):
    x = 2 ** -n
    a = (x ** 2 + 1) ** 0.5 - 1
    b = x ** 2 / ((x ** 2 + 1) ** 0.5 + 1)
    print(n, a, b, sep="\t")

# Wiarygodne wyniki otrzymujemy z drugiego wyrażenia (b)