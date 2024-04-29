lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def paros_szamok(lista):
    parosak = []
    for szam in lista:
        if szam % 2 == 0:
            parosak.append(szam)
    return parosak
parosak = paros_szamok(lista)
print(parosak)



def szavak_szama(szoveg):
    szavak = szoveg.split()
    return len(szavak)
mondat = "Ez egy őélda mondat you suckh"
szavak = szavak_szama(mondat)
print(szavak)



import random

def min_max_kulonbseg(lista):
    min_szam = min(lista)
    max_szam = max(lista)
    kulonbseg = max_szam - min_szam
    return kulonbseg
szamok = [random.randint(0, 100)for i in range(10)]


def atlag_es_indexek(lista):
    osszeg = sum(lista)
    atlag = osszeg / len(lista)
    nagyobbak = [i for i in range(len(lista)) if lista[i] > atlag]
    return atlag, nagyobbak
