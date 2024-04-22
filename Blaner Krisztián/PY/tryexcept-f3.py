"""3. Feladat
Hozz létre egy szöveges állományt, amely tartalmaz két számot egymástól tabulátorral elválasztva!
Írj egy programot, amely beolvassa a fájl tartalmát, és a képernyőn megjeleníti a két szám hányadosát!
A programot készítsd fel az esetleges hibalehetőségekre, a felhasználó pedig kapjon a hibának megfelelő figyelmeztető üzenetet ilyen esetben!"""

try:
    f = open("try.txt","r")
except:
    raise Exception(f"a file nem található vagy olvasható")


try:
    line = f.readline()
    print(line)
except:
    raise Exception(f"a file üres")


try:
    line = line.split(" ")
    print(line)
    x = int(line[0])
    y = int(line[1])
except:
    raise Exception("a file nem tartalmaz 2 számot szóközzel elválasztva")

try:
    print(round(x/y, 3))
except:
    raise Exception("A két szám nem osztható egymással")