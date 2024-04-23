import random
lista = []
lista_paros = []
for i in range(5):
    szam = random.randint(1,10)
    lista.append(szam)
    if(szam % 2 == 0):
        lista_paros.append(szam)
print(lista)
print(lista_paros)

szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']

darab = 0
for szo in szavak:
    if szo[0] == 'A' or szo[0] == 'a':
        darab += 1
        print(szo)
print(darab)

szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']


