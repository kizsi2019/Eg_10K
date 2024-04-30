with open('./10. Fájlkezelés/gyumolcsok.txt', 'r', encoding='utf-8') as forrasfajl, \
        open('./10. Fájlkezelés/gyumolcsok_masolat.txt', 'w', encoding='utf-8') as celfajl:
        for sor in forrasfajl:
            print(sor.strip(), file=celfajl)
  