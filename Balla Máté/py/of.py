"""""
class Haromszog:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
	    self.c = c

    def terulet(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def kerulet(self):
        return self.a + self.b + self.c


a = float(input("Kérem a háromszög 'a' oldalát: "))
b = float(input("Kérem a háromszög 'b' oldalát: "))
c = float(input("Kérem a háromszög 'c' oldalát: "))
h = Haromszog()
print(f"A háromszög területe: {h.terulet()}")
print(f"A háromszög kerülete: {h.kerulet()}")


class Diak:
    def __init__(self, nev, jegyek):
        self.nev = nev
        self.jegyek = jegyek
    
    def atlag(self):
        return sum(self.jegyek) / len(self.jegyek)
    
    def jegyek_fajlba(self, fajlnev):
        with open(fajlnev, "w") as f:
            f.write(f"{self.nev} jegyei:\n")
            for jegy in self.jegyek:
                f.write(str(jegy) + "\n")
                
nev = input("Kérem a diák nevét: ")
jegyek = []
while True:
    jegy = input("Kérem a jegyet (vagy írja be a 'q'-t a kilépéshez): ")
    if jegy == "q":
        break
    jegyek.append(int(jegy))

diak = Diak(nev, jegyek)
print(f"{diak.nev} átlaga: {diak.atlag()}")
diak.jegyek_fajlba("jegyek.txt")

class Szoba:
    def __init__(self, azonosito, ferohely):
        self.azonosito = azonosito
        self.ferohely = ferohely
        self.foglalt = False
    
    def foglal(self):
        self.foglalt = True
        
    def szabad(self):
        self.foglalt = False

szobak = [
    Szoba("101", 2),
    Szoba("102", 1),
    Szoba("103", 4),
    Szoba("201", 3),
    Szoba("202", 2),
    Szoba("203", 1),
]

datum = input("Kérem a dátumot (YYYY-MM-DD): ")

szabad_szobak = []
for szoba in szobak:
    if not szoba.foglalt:
        szabad_szobak.append(szoba)

szabad_szobak_fajlba = []
for szoba in szabad_szobak:
    szabad_szobak_fajlba.append(f"{szoba.azonosito} ({szoba.ferohely} fő)")

with open("szabad_szobak.txt", "w") as f:
    f.write(f"Szabad szobák a következő dátumra: {datum}\n\n")
    if szabad_szobak_fajlba:
        f.write("\n".join(szabad_szobak_fajlba))
    else:
        f.write("Nincsenek szabad szobák.")

class Termek:
    def __init__(self, nev, ar, keszlet):
        self.nev = nev
        self.ar = ar
        self.keszlet = keszlet

termekek = [
    Termek("Telefon", 49990, 5),
    Termek("Laptop", 149990, 3),
    Termek("Tablet", 79990, 2),
]

rendeles = input("Kérem a rendelni kívánt termék nevét: ")

for termek in termekek:
    if termek.nev.lower() == rendeles.lower():
        if termek.keszlet > 0:
            mennyiseg = int(input("Kérem a rendelt mennyiséget: "))
            if mennyiseg <= termek.keszlet:
                osszeg = mennyiseg * termek.ar
                termek.keszlet -= mennyiseg
                print(f"A rendelés összege: {osszeg}")
            else:
                print("Nincs elegendő készlet.")
        else:
            print("Nincs készleten.")
        break
else:
    print("Nem található ilyen termék.")

keszlet_fajlba = []
for termek in termekek:
    keszlet_fajlba.append(f"{termek.nev}: {termek.keszlet} db")

with open("keszlet.txt", "w") as f:
    f.write("\n".join(keszlet_fajlba))

class Auto:
    def __init__(self, tipus, ar, db):
        self.tipus = tipus
        self.ar = ar
        self.db = db

autok = [
    Auto("Suzuki Swift", 3490000, 5),
    Auto("Opel Corsa", 3790000, 3),
    Auto("Toyota Yaris", 4190000, 2),
]

vasarlas = input("Kérem a vásárolni kívánt autó típusát: ")

for auto in autok:
    if auto.tipus.lower() == vasarlas.lower():
        if auto.db > 0:
            db = int(input("Kérem a vásárolni kívánt darabszámot: "))
            if db <= auto.db:
                osszeg = db * auto.ar
                auto.db -= db
                print(f"A vásárlás összege: {osszeg}")
            else:
                print("Nincs elegendő készlet.")
        else:
            print("Nincs készleten.")
        break
else:
    print("Nem található ilyen autó típus.")

darabszamok_fajlba = []
for auto in autok:
    darabszamok_fajlba.append(f"{auto.tipus}: {auto.db} db")

with open("darabszamok.txt", "w") as f:
    f.write("\n".join(darabszamok_fajlba))
"""
class Osztok:
    def __init__(self, szam):
        self.szam = szam

    def osztok(self):
        osztok = []
        for i in range(1, self.szam + 1):
            if self.szam % i == 0:
                osztok.append(i)
        return osztok

    def prim(self):
        if self.szam < 2:
            return False
        for i in range(2, int(self.szam ** 0.5) + 1):
            if self.szam % i == 0:
                return False
        return True

szam = int(input("Kérem adjon meg egy egész számot: "))

osztok = Osztok(szam).osztok()
if Osztok(szam).prim():
    print(f"A(z) {szam} prímszám.")
else:
    print(f"A(z) {szam} nem prímszám.")
print(f"A(z) {szam} osztói: {osztok}")
