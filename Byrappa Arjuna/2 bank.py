def paros (szam):
    for szam in szamok:
        if szam % 2 == 0:
            print(szam)

szamok = [2,4,5,6,7,8]
paros(szamok)


'2. Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja a listában található legnagyobb számot.'

def legnagyobb (szam):
    x = max(szam)
    print(f"legnagyobb szam: {x}")

lista = [3,9,4,3]
legnagyobb(lista)


'3. Készíts egy függvényt, amely egy adott szöveget vár bemenetként, majd visszaadja a szövegben található szavak számát.'

'''def szavak (szo):
    for szo in lista:

        
lista = len(["bruh, bruh, bruh, bruh, bruh, bruh,"])
szavak(lista)'''


"4. Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja a listában található számok átlagát."

def atlag (szam):
    atlag = sum(szam) / len(szam)
    print(atlag)

szamok = [2,3,4,5]
atlag(szamok)

"Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja a listában található legkisebb és legnagyobb szám közötti különbséget."

def minmax (szam):
    minmax = max(szam) - min(szam)
    print(minmax)

szamok = [1,9]
minmax(szamok)