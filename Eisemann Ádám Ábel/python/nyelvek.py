nyelvek = []

with open('nyelvek.txt', 'r', encoding='utf-8') as forrasfajl, \
    open('nyelvek_masolat_2.txt', 'w', encoding='utf-8') as celfajl:
    for sor in forrasfajl:
        szavak = sor.strip().split(';')
        print(szavak[0], szavak[1], file=celfajl)

print(f'{nyelvek=}')


