szamok = []
szam = input("Kérek számokat: ")


while szam != "":
    szamok.append(int(szam))
    szam = input("Kérek számokat: ")

legkisebb = szamok[0]
legnagyobb = szamok[0]

for i in szamok:
    if i < legkisebb:
        legkisebb = i
    if i > legnagyobb:
        legnagyobb = i

print(szamok)
print(f"A legkisebb szám: {legkisebb}")
print(f"A legnagyobb szám: {legnagyobb}")
