
programozási_nyelvek = []
with open('prognyelv.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        prognyelv = {'year': int(adatok[0]), 'prognyelv': adatok[1], 'firstname': adatok[2], 'lastname': adatok[3]}
        programozási_nyelvek.append(prognyelv)

print(f'{ programozási_nyelvek=}')
    