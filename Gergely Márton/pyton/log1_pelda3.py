szam = int (input("Adj meg egy számot!"))

if szam %3 == 0:
    print("3-mal osztható")
if szam % 4 == 0:
    print("A szám 4-el osztható")
if szam % 3 and 4 == 0:
    print("A szám 3-mal és 4-el is osztható")
if szam % 3 == 1 or szam % 4 == 1:
    print("A szám 3-mal és 4-el sem osztható")