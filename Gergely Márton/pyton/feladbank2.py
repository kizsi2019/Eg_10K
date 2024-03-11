def legnagyobb_szam(szamok):
    maximum_szam = szamok[0]
    for szam in szamok:
        if szam > maximum_szam:
            maximum_szam = szam
    return maximum_szam

print(legnagyobb_szam([5, 7, 2, 8, 3, 9, 1, 6]))