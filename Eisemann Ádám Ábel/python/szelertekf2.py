'''lista = []
szam = input('Adj meg egy egész számot!')
while szam != "x" and szam != "X":
    lista.append(int(szam))
    szam = input("adj meg egy egész számot!")
print(lista)
legkisebb = lista[0]
legnagyobb = lista[0]
for szam in lista:
    if szam < legkisebb and szam % 2 == 0:
        legkisebb = szam
    if szam > legnagyobb and szam % 2 == 0:
        legnagyobb = szam

print(f'A legkisebb szám a listában: {legkisebb}')
print(f'A legnagyobb szám a listában: {legnagyobb}')  

'''
szavak = []
szo = input('Adj meg egy szót!')

while szo != "":
    szavak.append(szo)
    szo = input('Adj meg egy szót!')

legkisebb = szavak[0]
legnagyobb = szavak[0]

for szo in szavak:
    if len(szo) < len(legkisebb):
        legkisebb = szo
    if len(szo) > len(legnagyobb):
        legnagyobb = szo

print(f'A legkisebb szo a listában: {legkisebb}')
print(f'A legnagyobb szo a listában: {legnagyobb}') 

