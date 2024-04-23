lista = []

while True:
    szam = input("Adjál meg egy egész számot")
    szam = szam.lower()
    if szam == "x":
        break
    szam = int(szam)
    lista.append(int(szam))
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

