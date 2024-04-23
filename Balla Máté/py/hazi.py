with open('adatok.txt', 'r', encoding='utf-8') as bemeneti_fajl:
    sorok = bemeneti_fajl.readlines()

szurt_sorok = []
for sor in sorok:
    reszek = sor.strip().split(';')
    if len(reszek) >= 2:
        nyelv, ev = reszek[1], reszek[0]
        szurt_sorok.append(f"{nyelv}, {ev}\n")

with open('output.txt', 'w', encoding='utf-8') as kimeneti_fajl:
    kimeneti_fajl.writelines(szurt_sorok)

print("A fájl tartalma sikeresen másolva az új fájlba!")
