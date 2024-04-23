#1. Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja az összes páros számot a listában.
szamok=[1,2,3,5,2,1,6,8,6,5,4,4,6,8]
def paros(szamok):
    for i in szamok:
        if i%2==0:
            print(i)
paros(szamok)









