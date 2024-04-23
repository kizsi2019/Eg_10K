class Osztaly:
    def __init__(self,nev,jegy):
        self.fiuk = fiuk
        self.lanyok = lanyok

    def kiir(self):
        print("Fiuk", self.fiuk)
        print("Lányok", self.lanyok)

    def kiiras_fajlba(self):
        with open("osztaly.txt", "w", encoding= 'utf8') as f:
            f.write(f"Fiuk: {self.fiuk}\n")
            f.write(f"Lanyok: {self.lanyok}\n")

osztaly = Osztaly(15, 20)
oszaly.kiir()
osztaly.kiiras_fajlba()