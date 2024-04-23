#3. Készíts egy függvényt, amely egy adott szöveget vár bemenetként, majd visszaadja a szövegben található szavak számát.
szoveg=input("Írj be egy szöveget: ")
def szoveg_szam(szoveg):
    print(len(szoveg.split()))
szoveg_szam(szoveg)
