#9. Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja a lista elemeit megfordítva.
szamok=[1,2,3,5,2,1,6,8,6,5,4,4,6,8]
def fordit(lista):
    return lista[::-1]

print(fordit(szamok))