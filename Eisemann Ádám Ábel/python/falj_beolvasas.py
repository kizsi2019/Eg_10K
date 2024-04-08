''''
    # fajl megnyitása
forrasfajl = open('adatok/autok_listaja.csv')    
    
    # fájl tartalmának beolvasása
    # egy sor beolvasása:
forrasfajl.readline()

    # a teljes fájltartalom beolvasása
    # listával tér vissza, a sorok a lista elemei
forrasfajl.readlines()

    # a teljes fájltartalom beolvasása
forrasfajl.read()

    # a fájlobjektum tartalmanak bejarasa
for sor in forrasfajl:
    print(sor)

    # fájl bezárása    
forrasfajl.close() 
    '''


autok = []
with open('autok_listaja.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        auto = {'rendszam': adatok[0], 'tipus': adatok[1], 'kor': int(adatok[2])}
        autok.append(auto)

print(f'{autok=}')
    