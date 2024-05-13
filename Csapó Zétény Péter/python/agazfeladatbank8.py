import random

def atlag_es_index(lista):
    osszeg = sum(lista)
    atlag = osszeg / len(lista)
    nagyobbak = [i for i in range (len(lista)) if lista[i] > atlag]
    return atlag, nagyobbak

#felhasznalótól bekért lista
szamok = []
szam = input("Adja meg a számot: ")
while szam != "":
    szamok.apped(int(szam))
    szam = input("Adja meg a számot (Enterrel kilép): ")
