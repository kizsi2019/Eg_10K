import random
lista = []
osszeg = 0
for i in range(5):
    szam = random.randit(1, 10)
    lista.append(szam)
    osszeg += szam
print(lista)
print(osszeg)

