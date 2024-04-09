
számok = []


for i in range(3):
    while True:
        try:
            szám = int(input(f"Írd be a számot: "))
            break
        except ValueError:
            print("Rendes számot írjál be.")
    számok.append(szám)

print("Ezek a számok amit beírtál:")
for szám in számok:
    print(szám)