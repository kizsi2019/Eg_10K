import random
def paros_szamok(lista):
    parosak = []
    for szam in lista:
        if szam % 2 == 0:
            parosak.append(szam)
    return parosak

# Felhasnzálótól bekért lista
szamok = []
n = int(input("Adja meg a lista hosszát: "))
for i in range(n):
    szam = int(input("Adja meg a(z) {}. számot: ".format(i+1)))