programozasinyelvek = []
with open('10. Fájlkezelés\programnyelvek.csv', 'r', encoding='utf-8') as forrasfajl:
        for sor in forrasfajl:
            adatok = sor.strip().split(';')
            programnyelv = {'year': adatok[0], 'programminglanguange': adatok[1], 'firstname': adatok[2], 'lastname': adatok[2]}
            programozasinyelvek.append(programnyelv)

print(f'{programozasinyelvek=}')