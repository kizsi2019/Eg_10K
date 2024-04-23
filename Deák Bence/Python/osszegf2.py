lista = []
osszeg = 0

while True:
    szam = int(input("Kérek számokat -5 és 5 között: "))
    if szam <= 5 and szam >= -5:
        lista.append(szam)
    else:
        break

for i in lista:
    osszeg += i

print(f"A lista elemei: {lista}")
print(f"A számok összege: {osszeg}")
