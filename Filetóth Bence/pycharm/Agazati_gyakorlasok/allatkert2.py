class Allatkert:
    def __init__(self, novenyek, allatok):
        self.novenyek = novenyek
        self.allatok = allatok
    def kiir_novenyek_allatok_szama(self):
        print("Növények: ", self.novenyek)
        print("Állatok: ", self.allatok)
    def kiir_textbe(self):
        with open("allatkert2.txt", 'w', encoding='utf-8') as f:
            f.write(f"Növények: {self.novenyek}\n")
            f.write(f"Állatok: {self.allatok}\n")

szek = Allatkert(45, 67)
szek.kiir_novenyek_allatok_szama()
szek.kiir_textbe()
