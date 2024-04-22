with open('programozási_nyelvek.txt', 'r', encoding='utf-8') as forrasfajl, \
    open('programozási_nyelvek_másolat.txt', 'w', encoding='utf-8') as celfajl:
        for sor in forrasfajl:
            szavak = sor.strip().split(';')
            print(szavak[0], szavak[1], file=celfajl)