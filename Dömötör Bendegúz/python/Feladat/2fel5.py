szamlista = [1,2,5,7,23,3,8,78]

def parosszamok(szamlista):
    parosak = []
    for szam in szamlista:
        if szam % 2 == 0:
            parosak.append(szam)
    return parosak

print(parosszamok(szamlista))