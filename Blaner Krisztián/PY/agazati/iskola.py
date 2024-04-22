class iskola:
    def __init__(self,fiuk:int,lanyok:int):
        self.fiuk = fiuk
        self.lanyok = lanyok
    def letszam(self):
        return f"Fiúk: {self.fiuk}\nLányok: {self.lanyok}"
    def createtext(self):
        with open("suli.txt", "w", encoding="utf-8") as file:
            file.write(self.letszam())

SULI = iskola(142,81)

print(SULI.letszam())
SULI.createtext()