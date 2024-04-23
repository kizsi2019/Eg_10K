program = []
with open('program.csv', 'r',encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')                                        
        programok= {'year': int(adatok[0]), 'programing langue': adatok[1], 
        'first_name': (adatok[2]),
         'last_name':(adatok[3])}
        program.append(programok)
print(f'{program=}')    