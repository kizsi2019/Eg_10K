"""1. Feladat
Írj egy programot, ami a felhasználótól három egész számot számot kér be egyesével, ezeket eltárolja egy listában,
 majd a képernyőre kiírja a lista tartalmát! Ha a felhasználó nem számot ad meg, kapjon hibaüzenetet, és ismétlődjön meg a bekérés!"""

list = []
while True:
    if len(list) != 3:
        try:
            x = input("adjon meg egy egész számot>>>")
            x = int(x)
            list.append(x)
        except:
            print("Ez nem egy szám, list ujra bekérése")
            list.clear()
    else:
        print(list)
        break

