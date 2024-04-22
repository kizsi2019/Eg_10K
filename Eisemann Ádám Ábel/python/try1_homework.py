numbers = []

while len(numbers) < 3:
    try:
        num = int(input("Kérem adjon meg egy számot:  "))
        numbers.append(num)
    except ValueError: print("Hiba: Csak egész számokat adjon meg. ")
print("A megadott számok listája:", numbers)
