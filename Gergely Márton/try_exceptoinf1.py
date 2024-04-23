MAX_TRIES = 3  

szamok = []

for i in range(MAX_TRIES):
    try:
        szam = int(input(f"Adj meg egy egész számot a {i+1}. számnak: "))
        
        szamok.append(szam)
    except ValueError:
        print(f"Hibás érték! A {i+1}. számnak egy egész számot kell lennie.\n")

print("\nA beolvasott számok:")
for szam in szamok:
    print(szam)