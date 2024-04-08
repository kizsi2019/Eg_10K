hazifeladat = []
with open('hazifeladat.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        program_nyelv = {'year': int(adatok[0]), 
        'programming language': adatok[1], 
        'first name': adatok[2], 
        'last name': adatok[3]}
        hazifeladat.append(program_nyelv)

print(f'{hazifeladat=}')