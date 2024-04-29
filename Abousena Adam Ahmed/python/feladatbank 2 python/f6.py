import random

def min_max_kulonbseg(lista):
    min_szam = min(lista)
    max_szam = max(lista)
    kulonbseg = max_szam - min_szam
    return kulonbseg

# Felhasználótól bekért lista
szamok = []
szam = input("Adja meg az első számot: ")
while szam != "":
    szamok.append(int(szam))
    szam = input("Adja meg a következő számot (Enterrel kilép): ")
    
# Véletlenszerűen generált lista
# szamok = [random.randint(0, 100) for i in range(10)]

kulonbseg = min_max_kulonbseg(szamok)
print(kulonbseg)