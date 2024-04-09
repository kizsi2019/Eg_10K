while True:
    try:
        szam1 = float(input("Írd be az első számot: "))
        szam2 = float(input("Írd be a második számot: "))
        if szam2 == 0:
            raise ValueError("Nem lehet nullával osztani.")
        break
    except ValueError as hiba:
        print(hiba) 
        print("Rendes számot írjál be.")

hanyados = szam1 / szam2
print(f"A hányados {hanyados:.3f}")