try: 
    with open("szoveg.txt", "r") as file: 
        sor = file.readline().strip().split('\t') 
        szam1 = float(sor[0]) 
        szam2 = float(sor[1]) 
        if szam2 == 0: 
            print("Hiba: Nullával nem lehet osztani!") 
        else: print("A két szám hányadosa:", szam1 / szam2) 
except FileNotFoundError: 
    print("Hiba: A fájl nem található!") 
except ValueError: 
    print("Hiba: Nem megfelelő formátum a fájlban!")