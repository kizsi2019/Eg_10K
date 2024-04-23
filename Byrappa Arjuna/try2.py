def osztas():
    while True:
        try:
            szam1 = float(input("szam:"))
            szam2 = float(input("szam2: "))
            szamok = round(szam1 / szam2, 3)
            print("eredmeny: ", szamok)
            break
        except ValueError:
            print("Csak számokat!")
        except:
            if szam1 == 0:
                print('nulla nem lehet')
            if szam2 == 0:
                print('nulla nem lehet')
        
        #except ZeroDivisionError:
            #print("Hiba: Nullával nem lehet osztani.")

osztas()