import random

lista = []
for i in range(5):
    lista.append(random.randint(1, 20))

print(lista)


def listaszam(a):
    osszeg = 0
    for i in a:
        osszeg += i
    print(osszeg)


listaszam(lista)
