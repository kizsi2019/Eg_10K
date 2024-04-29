szamlista = [454,123,742,666,631,107]
darabszam = ""



def atlag(szamlista):
    osszeg = 0
    for szam in szamlista:
        osszeg += szam
    return osszeg / len(szamlista)

print(atlag(szamlista))