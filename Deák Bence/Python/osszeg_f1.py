import random

lista = []
osszeg = 0
for i in range(5):
    szam = random.randint(1, 10)
    lista.append(szam)

for szamok in lista:
    if szamok % 2 == 0:
        osszeg += szamok

print(lista)
print(osszeg)
