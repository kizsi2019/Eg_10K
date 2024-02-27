def atlag_szamoknak(szamlista):
    osszeg = sum(szamlista)
    atlag = osszeg / len(szamlista)
    return atlag

szamlista = [5, 4, 2, 3, 5, 2, 4, 3, 6]
print("A számok átlaga:", atlag_szamoknak(szamlista))
