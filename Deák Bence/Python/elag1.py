userszam = int(input("Kérek egy számot: "))

if userszam < 0:
    print("A szám negatív.")
elif userszam == 0:
    print("A szám nulla.")
else:
    print("A szám pozitív.")

if userszam % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan")
print("Finito.")
