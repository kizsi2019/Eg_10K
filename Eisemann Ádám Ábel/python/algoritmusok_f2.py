szamok = int(input('Adj meg számot -5 és 5 között: '))
osszeg = 0
szam = []
while(-5 <=szamok <= 5):
    szam.append(szamok)
    osszeg += szamok
    szamok = int(input("adj meg egy szamot -5 és 5 között"))
print(szamok)
print(f"Az összegük: (osszeg)")