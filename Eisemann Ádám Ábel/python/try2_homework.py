#Írj egy programot, ami a felhasználótól bekér két számot, és a képernyőn megjeleníti a két szám hányadosát három tizedesjegy pontossággal! A program adjon hibaüzenetet, ha a felhasználó nem számot adott meg, vagy az osztás nem végezhető el! Ebben az esetben kérjen be újabb adatot mindaddig, amíg nem lép fel hiba!
try: 
    num1 = float(input("Adj meg egy számot: "))
    num2 = float(input("Adj meg mégegy számot: "))

    print(f"A két szám hányadosa: {num1/num2:.3f}")
except ZeroDivisionError as e: 
    print("Hiba: ", e)
    print("0 val nem lehet osztani.")
except ValueError as i: 
    print("Hiba: ", i)
    print("Hiba: Számot irj be")



