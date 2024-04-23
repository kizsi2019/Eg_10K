szam = int(input("Adj meg egy számot!"))
if szam % 3 == 0:
    print("A szám oztható hárommal!")
if szam % 4 == 0:
    print("A szám osztható néggyel!")
if szam % 3 ==0 and szam % 4 == 0:
    print("A szám osztható hárommal és néggyel.")
if szam % 3 == 1 or szam % 4 == 1:
    print("A szám hárommal és néggyel sem osztható! ")   