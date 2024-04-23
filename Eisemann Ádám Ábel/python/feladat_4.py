def atlag(szamok):
    osszeg = 0
    for szam in szamok:
        osszeg += szam
    return osszeg / len(szamok)

# Példa használat:
szamok = [3, 7, 3, 8, 5]
print(atlag(szamok))  
