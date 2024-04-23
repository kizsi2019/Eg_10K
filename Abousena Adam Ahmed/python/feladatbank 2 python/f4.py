'''4. Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja a listában található számok átlagát.'''

def atlag(szamok):
    total = sum(szamok)
    atlag = total / len(szamok)
    return atlag

szamok = [1, 2, 3, 4, 5]
atlag = atlag(szamok)
print(atlag)  