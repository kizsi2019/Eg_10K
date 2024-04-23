while True: 
    try: 
        szam1 = float(input("Kérem, adjon meg egy számot: ")) 
        szam2 = float(input("Kérem, adjon meg még egy számot: ")) 
        if szam2 == 0: 
            print("Hiba: Nullával nem lehet osztani! Kérem, adjon meg új számokat.") 
            continue 
        hanyados = szam1 / szam2 
        print("A két szám hányadosa három tizedesjegy pontossággal:", "{:.3f}".format(hanyados)) 
        break 
    except ValueError: 
        print("Hiba: Csak számokat lehet megadni! Kérem, próbálja újra.")