class Allatkert:
    def __init__(self):
        self.novenyek = 0
        self.allatok = 0

    def kiir_allatok_novenyek(self):
        print(f"Az allatkertben {self.allatok} állat és {self.novenyek} növény található.")

    def fajlba_ir_allatok_novenyek(self):
        with open("allatkert.txt", "w") as f:
            f.write(f"Az allatkertben {self.allatok} állat és {self.novenyek} növény található.")

allatkert = Allatkert()

allatkert.kiir_allatok_novenyek()
allatkert.fajlba_ir_allatok_novenyek()