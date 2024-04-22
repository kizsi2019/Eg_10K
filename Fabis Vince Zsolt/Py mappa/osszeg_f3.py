szamok = []
osszeg = 0

szam = int(input('Adj meg egy számot -5 és 5 között'))
while(-5 <= szam <= 5):
    szamok.append(szam)
    osszeg += szam
    szam = int(input("Adj meg egy számot"))

print(szamok)
print(osszeg)