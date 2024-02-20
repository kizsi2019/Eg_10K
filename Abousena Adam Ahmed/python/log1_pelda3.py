szam = int(input("Adj meg egy számot"))
if szam % 3 == 0:
    print("3-mal osztható")
if szam % 4 == 0:
    print("A szám 4-gyel osztható")
if szam % 3 and 4 == 0:
    print("A szám 3-mal és 4-gyel osztható")
if szam % 3 == 1 or szam % 4 == 1:
    print("A szám sem 3-mal, sem 4-gyel nem osztható")
