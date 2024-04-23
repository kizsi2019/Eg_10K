szam = int(input("Szám: "))


def szamolo(a):
    if a > 0:
        print("A szám pozitív.")
    elif a < 0:
        print("A szám negatív.")
    else:
        print("A szám nulla.")


szamolo(szam)
