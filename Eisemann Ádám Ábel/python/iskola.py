class Osztaly:
    def __init__(self,fiuk,lanyok):
        self.fiuk = fiuk
        self.lanyok = lanyok

    def kiir(self):
        print("Fiuk: ", self.fiuk)
        print("Lanyok: ", self.lanyok)

    def kiiras_fajlba(self):
        with open('osztaly.txt', 'w', encoding='utf-8') as f:
            f.write(f"fiúk: {self.fiuk}\n")
            f.write(f"Lányok: {self.lanyok}\n")

osztaly = Osztaly(21,25)
osztaly.kiir()
osztaly.kiiras_fajlba()

