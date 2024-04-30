"""2. Feladat
Írj egy programot, ami a felhasználótól bekér két számot,
és a képernyőn megjeleníti a két szám hányadosát három tizedesjegy pontossággal!
A program adjon hibaüzenetet, ha a felhasználó nem számot adott meg, vagy az osztás nem végezhető el!
Ebben az esetben kérjen be újabb adatot mindaddig, amíg nem lép fel hiba!"""

while True:
    try:
        x = input("adja meg a számot amit a követező bevitellel fog osztani>>>")
        x = float(x)
        y = input("adja meg az osztó egész számot")
        y = float(y)
        print(round(x/y,3))
        break
    except:
        print("hiba történt vagy nem számot adott meg vagy 0 az osztó!")

