while True:
    try:
        szam1 = float(input("Adj meg egy számot: "))

        szam2 = float(input("Adj meg egy másik számot: "))

        print(f"A két szám hányadosa: {szam1 / szam2:.3f}")

        break
    except ValueError:
        print("Hibás érték! A bemenetnek számnak kell lennie.\n")
    except ZeroDivisionError:
        print("Hibás érték! A második szám nem lehet nulla.\n")