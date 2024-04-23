userszam = int(input("Kérek egy számot: "))

if userszam % 3 == 0 and userszam % 4 == 0:
    print("A szám hárommal és néggyel is osztható.")
elif userszam % 4 == 0:
    print("A szám csak néggyel osztható.")
elif userszam % 3 == 0:
    print("A szám csak hárommal osztható.")
else:
    print("A szám nem osztható egyikkel sem.")
