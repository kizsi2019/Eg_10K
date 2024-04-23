#4. Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja a listában található számok átlagát.
szamok=[1,2,3,5,2,1,6,8,6,5,4,4,6,8]
def atlag(szamok):
    print(sum(szamok)/len(szamok))
atlag(szamok)