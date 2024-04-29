def paros_szamok(lista):
    parosak = [] 
    for szam in lista:
        if szam % 2 == 0:
            parosak.append(szam)
    return parosak

lista = [1, 2, 3, 4, 5, 6, 7]
parosak = paros_szamok(lista)
print("Az összes páros szám a listában:", parosak)
