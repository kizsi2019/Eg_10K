import random

def atlag_ex_indexek(lista):
    osszeg = sum(lista)
    atlag = osszeg / len(lista)
    nagyobbak = [i for i in range(len(lista)) if lista[i] > atlag]
    return atlag, nagyobbak