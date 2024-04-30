szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("És mégegyet: "))


def szamolosdi(a, b):
    if a > b:
        print(f"{a} nagyobb, mint {b}.")
    elif b > a:
        print(f"{b} nagyobb, mint {a}.")
    else:
        print("A két szám egyenlő.")


szamolosdi(szam1, szam2)
