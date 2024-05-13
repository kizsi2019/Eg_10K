def lista_forditott(lista):
    lista_forditott = lista[::-1]
    return lista_forditott

#felhasznalotól bekért lista
szamok = []
szam = input("Adja meg az első számot: ")
while szam != "":
    szamok.append(int(szam))
    szam = input = ("Adja meg a következő számot (Enterrel kilép): ")
