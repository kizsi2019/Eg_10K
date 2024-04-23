szamlist = []
osszeg = []
szamok = int(input('Adj meg egy számot -5 és 5 között: '))

while szamok > -6 and szamok < 6:
    szamlist.append(szamok)
    osszeg += szamok
    szamok = int(input('Adj meg egy számot -5 és 5 között: '))
    

print(szamlist)
print(osszeg)