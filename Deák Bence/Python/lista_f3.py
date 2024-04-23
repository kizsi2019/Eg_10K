import random

lista = []

for i in range(10):
    szam = random.randint(0, 51)
    if szam % 4 == 0:
        lista.append(szam)
print(lista)
print(len(lista))
