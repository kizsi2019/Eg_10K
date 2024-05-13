while True:
    hajonev = input("Adja meg a hajó nevét")
    gyartas = int(input("Írja be a hajó gyártási évét: "))

    if gyartas < 1950 or 2024 - gyartas < 10:
        print("A hajó nem éri el a minimum életkort")

    else:
        break

hajoev = 2024 - gyartas
print(f"Ezt írtad be: {hajoev}")
print(f"A hajó {hajoev} éves")
print(f"A hajó nevében{len(hajonev)} betű van")

def tavolsagok(menetido, sebesseg):
    return (menetido / 60) * sebesseg

menetido_perc = int(input("Írja be a hajózási idejét percben: "))
sebesseg_km_h = int(input("Írd be a hajónak a sebbességét km/h-ban: "))

tavolsag_km = tavolsagok(menetido_perc, sebesseg_km_h)
print(f"A megtett távolság {tavolsag_km} km.")

def szerviz(gyartas):
    hajoev = 2024 - gyartas
    if hajoev >= 10:
        print("A hajót évente kell szervízeli")
    elif hajoev >= 3:
        print("A hajót két évente kell szervízelni")
    else:
        print("A hajót 3 évente kell szervízelni")

gyartas = int(input("Íja be a hajó gyártási évét"))
szerviz(gyartas)

class ShipData:
    def __init__(self, nev, ev, tn, egytank):
        self.nev = nev
        self.ev = int(ev)
        self.tulaj_nev = tn
        self.egytank = int(egytank)

    def __str__(self):
        print(self.nev, self.nev)

with open("ship.txt", "rt", encoding="utf-8") as f:
    adatok = f.readLies()

adatok.pop(0)
adatok.pop(0)
ship = []

for i in adatok:
    s= i.split(";")
    ship_egyen = ShipData(s[0], s[1], s[2], s[3])
    ship.append(ship_egyen)

def legoregebb(lista):
    oldest = lista[0].ev
    for i in lista:
        if i.ev < oldest:
            oldest = i.ev
    return oldest

legoregebb(ship).__str__()

def km_1980_utan(lista):
    ossz_km = 0
    db = 0
    for i in lista:
        if i.ev > 1980:
            db +=1
            ossz_km += i.egytank

    return round(ossz_km / db, 2)

print(km_1980_utan(ship, "km"))