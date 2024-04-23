szamok = [] 
while len(szamok) < 3: 
    try: 
        num = int(input("Kérem adjon meg egy egész számot: ")) 
        szamok.append(num) 
    except ValueError: 
        print("Hiba: Csak egész számokat adjon meg.") 
print("A megadott számok listája:", szamok)