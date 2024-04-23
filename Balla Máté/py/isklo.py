class Osztaly:
    def __init__(self, fiuk, lanyok):
        self.fiuk = fiuk
        self.lanyok = lanyok

    def kiir(self):
        print("fiuk:", self.fiuk)
        print("lanyok:", self.lanyok)

    def kiiras_fajlba(self):
        with open("osztaly.txt", "w", encoding="utf-8") as f:
            f.write(f"fiuk: {self.fiuk}\n")
            f.write(f"lanyok: {self.lanyok}\n")

osztaly = Osztaly(15, 20)
osztaly.kiir()
osztaly.kiiras_fajlba()
