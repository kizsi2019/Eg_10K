szamlista = [454,123,742,666,631,107]
darabszam = ""



def atlag(szamlista):
    darabszam = szamlista.count
    for szam in szamlista:
        osszeg += szam
    atlag = osszeg / darabszam
    return atlag

print(atlag)