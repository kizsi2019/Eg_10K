szavak = []
szo = input("Kérek szavakat: ")

while szo != "":
    szavak.append(szo)
    szo = input("Kérek szavakat: ")

rovid = szavak[0]
hosszu = szavak[0]

for i in szavak:
    if len(i) < len(rovid):
        rövid = i
    if len(i) > len(hosszu):
        hosszu = i

print(szavak)
print(f"Legrövidebb szó: {rovid}")
print(f"Leghosszabb szó: {hosszu}")
