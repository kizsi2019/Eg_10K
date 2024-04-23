def paros_szamok(szamlista):
    parosok = []
    for szam in szamlista:
        if szam % 2 == 0:
            parosok.append(szam)
    return parosok

szamok = [13,7,4,1,13,102,91]
print(paros_szamok(szamok))
