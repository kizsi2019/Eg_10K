try:
    with open("szamok123.txt", "r") as file:
        tartalom = file.read().strip().split("\t")
        if len(tartalom) != 2:
            raise ValueError("Kettő szám között kell tab ot nyomni.")
        szám1, szám2 = map(float, tartalom)
        if szám2 == 0:
            raise ValueError("A második szám nem lehet 0.")
        eredmény = szám1 / szám2
        print(f"The result is {eredmény}.")
except FileNotFoundError:
    print("The file 'szamok123.txt' was not found.")
except ValueError as végeredmény:
    print(végeredmény)