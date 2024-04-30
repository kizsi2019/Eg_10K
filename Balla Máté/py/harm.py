def szavak_szama(szoveg):

    szavak = szoveg.split()
    return len(szavak)

beirt_szoveg = "Az alma le esett a farol bruh"
szavak_szam = szavak_szama(beirt_szoveg)
print(f"A szövegben található szavak száma: {szavak_szam}")
