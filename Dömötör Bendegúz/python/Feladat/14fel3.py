try:
    with open("szamok.txt", "r") as f:
        num1 = map(float, f.readline().strip().split("\t"))
        num2 = map(float, f.readline().strip().split("\t"))
except FileNotFoundError:
    print("A fájl nem található!")
except ValueError:
    print("A fájl tartalma hibás!")

try:
    hanyados = num1 / num2
    print(f"A két szám hányadosa: {hanyados}")
except ZeroDivisionError:
    print("A második szám nem lehet nulla!")
#NEM JÓ A KÓD