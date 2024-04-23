#6. Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja a listában található legkisebb és legnagyobb szám közötti különbséget.
szamok=[1,2,3,5,2,1,6,8,6,5,4,4,6,8]
def kulonbseg(szamok):
    print(max(szamok)-min(szamok))
kulonbseg(szamok)
