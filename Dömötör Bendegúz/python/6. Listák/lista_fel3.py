import random
lista = []
for i in range(10):
    szam = random.randint(1,50)
    if (szam % 4 == 0):
        print(szam)
    lista.append(szam)

print(lista)