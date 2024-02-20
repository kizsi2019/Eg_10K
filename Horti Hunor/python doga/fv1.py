def paros_szamok(lista):
    return [szam for szam in lista if szam % 2 == 0]

szamlista = [3123123, 23123123, 32426, 52354,]
print(paros_szamok(szamlista)) 
