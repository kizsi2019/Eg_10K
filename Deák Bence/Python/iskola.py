class Iskola:
    def __init__(self, fiuk, lanyok):
        self.fiuk = fiuk
        self.lanyok = lanyok

    def szamolo(self):
        print(f"A fiúk száma: {self.fiuk}")
        print(f"A lányok száma: {self.lanyok}")

    def fajlba_iras(self):
        with open("osztaly.txt", "w", encoding="utf-8") as f:
            f.write(f"Fiúk: {self.fiuk}\n")
            f.write(f"Lányok: {self.lanyok}\n")


osztaly01 = Iskola(3, 11)
osztaly01.szamolo()
osztaly01.fajlba_iras()
