szavak = []

szo = input("Adjál meg egy egész szót")
while szo != '':
    szavak.append(szo)
    szo = input("Adjál meg egy egész szót")
print(szavak)
legkisebb = szavak[0]
legnagyobb = szavak[0]
for szo in szavak:
    if len(szo) < len(legkisebb) :
        legkisebb = szo
    if len(szo) > len(legkisebb) :
        legnagyobb = szo






print(f'A legrövidebb szó a szavak közűl: {legkisebb}')
print(f'A leghosszabb szó a szavak közűl: {legnagyobb}')