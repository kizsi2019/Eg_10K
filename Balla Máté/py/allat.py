class Osztaly:
    def __init__(self, allatok, novenyek):
        self.allatok = allatok
        self.novenyek = novenyek

    def kiir(self):
        print("allatok:", self.allatok)
        print("novenyek:", self.novenyek)

    def kiiras_fajlba(self):
        with open("osztaly.txt", "w", encoding="utf-8") as f:
            f.write(f"allatok: {self.allatok}\n")
            f.write(f"novenyek: {self.novenyek}\n")

osztaly = Osztaly(45, 67)
osztaly.kiir()
osztaly.kiiras_fajlba()
