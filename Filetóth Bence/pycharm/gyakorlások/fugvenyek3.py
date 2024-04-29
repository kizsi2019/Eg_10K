lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]


def harommal_oszthato(lista):
    darab = 0
    for elem in lista:
        if elem % 3 == 0:
            darab += 1
    return darab


print(harommal_oszthato(lista))

szam = input("Adjál meg egy egész szót")
while szam >= 0:
    lista.append(szam)
    szam = input("Adjál meg egy egész szót")
def harommal_oszthato(lista):
    darab = 0
    for elem in lista:
        if elem % 3 == 0:
            darab += 1
    return darab