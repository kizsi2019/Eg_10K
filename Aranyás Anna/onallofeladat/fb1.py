szamok = [1, 2, 3, 4, 5]
def paros_szamok(lista):
    paros = [szam for szam in
lista if szam % 2 ==0]
    return paros

print(paros_szamok(szamok))