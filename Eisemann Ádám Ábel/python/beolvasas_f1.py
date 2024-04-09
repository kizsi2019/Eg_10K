programozasi_nyelvek = []
with open('programozas_nyelvek.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        program_nyelv = {'year': int(adatok[0]), 'programing language': adatok[1], 'firstname': adatok[2], 'Lastname': adatok[2]}
        programozasi_nyelvek.append(program_nyelv)

print(f'{programozasi_nyelvek=}')