def paros_szamok(szamok):
    return [num for num in szamok if num %2 == 0]
szamok = [1, 2, 3, 4, 5, 6]
print(paros_szamok(szamok))