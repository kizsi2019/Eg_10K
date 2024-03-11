def atlag_szamolo(szamlista):
    atlag = 0

    szamok_osszege = sum(szamlista)

    atlag = szamok_osszege / len(szamlista)

    return atlag

szamok = [1, 2, 3, 4, 5]
print(atlag_szamolo(szamok))