def atlag(szamlista):
    if len(szamlista) == 0:
        return 0  
    osszeg = sum(szamlista)
    atlag = osszeg / len(szamlista)
    return atlag


szamok = [10, 20, 30, 40, 50]
print(f"A számok átlaga: {atlag(szamok)}")
