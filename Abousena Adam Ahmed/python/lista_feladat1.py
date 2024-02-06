nevek = []

while True:
    nev = input("Adjon meg egy keresztnevet")
    if nev == "":
        break
    nevek.append(nev)

print("A bekért nevek:")
for nev in nevek:
    print(nev)