bekert_szam = int(input("Adj meg egy páros számot: "))
darab_karakter = 1
sor = 1
while sor <= bekert_szam / 2:
    oszlop = 1
    while oszlop <= darab_karakter:
        print("O ", end="")
        oszlop += 1
    print("")
    darab_karakter += 1
    sor += 1

darab_karakter = bekert_szam / 2
sor = 1
while sor <= bekert_szam / 2:
    oszlop = 1
    while oszlop <= darab_karakter:
        print("O ", end="")
        oszlop += 1
    print("")
    darab_karakter -= 1
    sor += 1
