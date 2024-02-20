szam =int(input("adj meg egy paros szamot:"))

darab_karaker = 1
sor = 1
while sor <= szam/2:
    oszlop = 1
    while oszlop <= darab_karaker:
        print('0', end= '')
        oszlop = oszlop + 1
    print('')
    darab_karaker = darab_karaker + 1
    sor = sor + 1

darab_karaker = szam/2
sor = 1
while sor <= szam/2:
    oszlop = 1
    while oszlop <= darab_karaker:
        print('0', end='')
        oszlop = oszlop + 1
    print('')
    darab_karaker = darab_karaker - 1
    sor = sor + 1