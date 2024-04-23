szam =int(input("adj meg egy szamot:"))

if szam % 3 == 0:
    print("a szam oszthato harommal")
if szam % 4 ==0:
    print("a szam oszthato néggyel")
if szam % 3 == 0 and szam % 4 ==0:
    print("3 mal és 4 el is oszthato a számod")
if szam % 3 == 1 or szam % 4 == 1:
    print("3 mal és 4 el sem lehet osztani")