programozasi_nyelvek = []
with open('programozasi_nyelvek.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        program_nyelv = {'year': adatok[0], 'programing language': adatok[1]}
        programozasi_nyelvek.append(program_nyelv)

print(f'{programozasi_nyelvek=}')