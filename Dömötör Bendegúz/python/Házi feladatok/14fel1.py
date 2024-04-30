szamok = []

for i in range(1, 4):
    while True:
        try:
            num = int(input(f"Adj meg egy egész számot a {i}. számra: "))
            szamok.append(num)
            break
        except ValueError:
            print("Hiba! Kérlek adj meg egy egész számot!")


print("A bekért számok:")
for num in szamok:
    print(num)