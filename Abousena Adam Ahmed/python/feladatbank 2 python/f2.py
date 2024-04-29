def legnagyobb_szam(lista):
    max_szam = lista[0]
    for szam in lista:
        if szam > max_szam:
            max_szam = szam
    return max_szam

szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
legnagyobb = legnagyobb_szam(szamok)
print(legnagyobb) # 10