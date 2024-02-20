def legnagyobb_szam(szamlista):
    legnagyobb = szamlista[0]
    for szam in szamlista:
        if szam > legnagyobb:
            legnagyobb = szam
    return legnagyobb

szamok = [1.1,1.2,1.23232]
print(legnagyobb_szam(szamok))
