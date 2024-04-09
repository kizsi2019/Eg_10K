while True: 
    try: 
        szam1 = float(input("Kérem adja meg az első számot: ")) 
        szam2 = float(input("Kérem adja meg a második számot: ")) 
        eredmeny = szam1 / szam2 
        print("Az eredmény:", round(eredmeny, 3)) 
        break 
    except ValueError: print("Hiba: Csak számokat adjon meg!") 
    except ZeroDivisionError: 
        print("Hiba: Nullával nem lehet osztani! Kérem adjon meg egy második számot!")