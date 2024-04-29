import random

def atlag_es_indexek(lista):
    osszeg = sum(lista)
    atlag = osszeg / len(lista)
    nagyobbak = [i for i in range(len(lista)) if lista [i] > atlag]
    return atlag, nagyobbak

# Felhasználótól bekért lista
szamok = []
szam = input("Adja meg az első számot:")
while szam != "":
    szamok.append(int(szam))
    szam = input("Adja meg a következő számot (Enterrel kilép): ")

# Véletlenszerűen generált lista
# szamok = [random.randint(0, 100) for i in range(10)]

atlag, nagyobbag = atlag_es_indexek(szamok)
print("Az átlag: ", atlag)
print("Az átlagnál nagyobb elemek indexei: ", nagyobbak)

