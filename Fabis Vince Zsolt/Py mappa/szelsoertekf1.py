lista = [0]
szam = input("Adj meg egy egész számot!")
while szam != 'X' and szam != 'x':   
    lista.append(int(szam))
    szam = input("Adj meg egy egész számot!")
print(lista)
legkisebb = lista[0]
legnagyobb = lista[0]

for szam in lista:
    if szam < legkisebb and szam  % 2 == 0:
        legkisebb = szam
    if szam > legnagyobb and szam % 2 == 0:
        legnagyobb = szam

print(f'A legkisebb szám a listában: {legkisebb}')
print(f'A legnagyobb szám a listában: {legnagyobb}')  