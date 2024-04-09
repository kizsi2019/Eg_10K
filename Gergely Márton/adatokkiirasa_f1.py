with open('nevek.txt', 'r', encoding= 'utf-8') as forrasfajl, \
    open("nevek_masolat.txt", "w", encoding= 'utf-8') as celfajl:
        for sor in forrasfajl:
            szavak = sor.strip( ).split(";")
            print(szavak[0], szavak[1], file=celfajl)