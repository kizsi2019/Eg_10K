szavak = []
szo = input("Adj meg egy szót!")
while szo != '':
    szavak.append(szo)
    szo = input("Adjál meg egy egész szót!")
print(szavak)
legkisebb = szavak[0]
legnagyobb = szavak[0]

for szo in szavak:
    if len(szo) < len(legkisebb):
        legkisebb = szo
    if len(szo) > len(legnagyobb):
        legnagyobb = szo

print(f'A legrövidebb szó a listában: {legkisebb}')
print(f'A leghosszabb szó a listában: {legnagyobb}')  