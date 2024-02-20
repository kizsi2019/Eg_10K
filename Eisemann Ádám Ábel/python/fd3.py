def szavak_szama(szoveg):
    
    szavak = szoveg.split()
    szavak_szama = len(szavak)
    return szavak_szama


szoveg = "Ez egy példa szöveg a szavak számának meghatározására."
eredmeny = szavak_szama(szoveg)
print("A szövegben található szavak száma:", eredmeny)
