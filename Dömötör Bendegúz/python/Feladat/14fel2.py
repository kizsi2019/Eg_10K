try:
    num1 = float(input("Adj meg egy számot: "))
    num2 = float(input("Add meg a számot: "))

    print(f"A hányadosuk: {num1 / num2:.3f}")
    
except ZeroDivisionError as e:
    print("Hiba", e)
    print("Nullával nem oszthatunk!")
except ValueError as i:
    print("Hiba", i)
    print("Kérlek számot adj meg!")
