import random

lista = []
paros_lista = []

for i in range(5):
    szam = random.randint(1, 10)
    lista.append(szam)
    if szam % 2 == 0:
        lista.append(szam)

print(lista)
print(len(lista))
