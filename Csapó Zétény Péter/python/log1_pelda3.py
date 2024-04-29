szam = int(input("Adj eg egy számot!"))
if szam % 3==0:
    print ("Hárommal osztható")
if szam % 4==0:
    print ("Néggyel osztható")
if szam % 3==0 and szam % 4==0:
    print("A szám hárommal és néggyel is osztható")
else:
    print("A szám se hárommal, se néggyel nem osztható")

