import random

tarolo = []

for i in range(4):
    lista = [random.randint(0, 25) for i in range(3)]
    tarolo.append(lista)

for lista in tarolo:
    print(lista)