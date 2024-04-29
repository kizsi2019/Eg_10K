class Allatkert:

    def __init__(self, novenyek, allatok):
        self.novenyek = novenyek
        self.allatok = allatok

    def szamolo(self):
        print(f"Növények száma: {self.novenyek}")
        print(f"Állatok száma: {self.allatok}")

    def fajlba_iras(self):
        with open("allatkert.txt", "w", encoding="utf-8") as f:
            f.write(f"Növények száma: {self.novenyek}\n")
            f.write(f"Állatok száma: {self.allatok}\n")


allatkert = Allatkert(12, 40)
allatkert.szamolo()
allatkert.fajlba_iras()
