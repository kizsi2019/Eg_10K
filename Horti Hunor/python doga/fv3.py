def szavak_szama(szoveg):
    szavak = szoveg.split()
    return len(szavak)

beirt_szoveg = "Itt a pelda mondat, ez 4 szo!."
print(szavak_szama(beirt_szoveg))  
