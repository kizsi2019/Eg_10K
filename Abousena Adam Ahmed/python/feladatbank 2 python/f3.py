'''3. Készíts egy függvényt, amely egy adott szöveget vár bemenetként, majd visszaadja a szövegben található szavak számát.'''
def szamolas(szo):
    szavak = szo.split()
    return len(szavak)

szo = "szia szia szia"
szamolas = szamolas(szo)
print(szamolas)  