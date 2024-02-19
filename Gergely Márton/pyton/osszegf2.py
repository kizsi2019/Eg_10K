szamok = []
osszeg = 0

szam = int(input("Adj meg egy számot"))
while(-5 <=szam <=5):
    szamok.append(szam)
    osszeg += szam
    szam = int(input("Adj meg egy számot"))

print(szamok)
print(f"Az osszegük: {osszeg}")
