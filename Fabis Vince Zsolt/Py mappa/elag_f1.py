szam = int(input("Adj meg egy számot"))
if szam > 0 and szam %2 ==0:
    print("A szám pozitív páros szám")
elif szam < 0 and szam %3 == 0:
    print("A szám negatív páratlan")
else:
    print("A szám nem felel meg a feltételeknek")
