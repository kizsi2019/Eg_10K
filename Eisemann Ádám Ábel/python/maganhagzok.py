def maganhangzok(szoveg):
    magy_maganhazok = ["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"
"A", "Á", "E", "É", "I", "Í", "O", "Ó", "Ö", "Ő", "U", "Ú", "Ü", "Ű"]
    magy_maganhazok_szam = 0
    for betu in szoveg:
        if betu in magy_maganhazok:
            magy_maganhazok_szam = +1
            return magy_maganhazok_szam







szoveg = str(input("Adjon meg egy szöveget: "))
print("Az összes magánhangzó száma a szövegben:", maganhangzok(szoveg))