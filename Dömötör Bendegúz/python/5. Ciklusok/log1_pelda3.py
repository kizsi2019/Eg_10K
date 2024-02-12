szam = int(input("Adj meg egy szamot: "))
if szam % 3 == 0:
    print("3-mal osztható.")
if szam % 4 == 0:
    print("4-gyel osztható.")
if szam % 3 == 0 and szam % 4 == 0:
    print("3-mal és 4-gyel is osztható.")
else:
    print("3-mal se 4-gyel sem osztható.")