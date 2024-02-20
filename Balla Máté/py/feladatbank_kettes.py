"""
1.
"""
def paros_e():
    lista = []
    while True:
            szam = input("Adj meg egy számot(kilepes exit): ")
            if szam == "exit":
                break
            szam = int(szam)  
            if szam % 2 == 0:
                lista.append(szam)
      
    if len(lista) > 0:
        print("Van páros szám a listában:", lista)
    else:
        print("Nincs páros szám a listában.")

paros_e()


"""
2.
"""
szamok = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def legnagyobb_szam(list):
    return max(list)

legnagyobb  = legnagyobb_szam(szamok)
print(f"A legnagyobb szám a listában: {legnagyobb}")

"""
3.
"""
szoveg = "kerekasztalon kerekesszekkel keretes képeket kereteznek"
def szavak_szama(szovegek):
    szavak = szovegek.split()
    return len(szavak)
szavak_szam = szavak_szama(szoveg)
print(f"A szövegben található szavak száma: {szavak_szam}")

"""
4.
"""
szamok2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def atlag(szamoklista):

    osszeg = sum(szamoklista)
    atlag = osszeg % len(szamoklista)
    return atlag
atlag_ertek = atlag(szamok2)
print(f"A számlista átlaga: {atlag_ertek}")