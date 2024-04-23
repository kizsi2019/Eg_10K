class Allatkert:
    def __init__(self, noveny,allatok):
        self.noveny = noveny
        self.allatok = allatok

    def kiir(self):
        print("Noveny: ", self.noveny)
        print("Allatok: ", self.allatok)

    def kiiras_fajlba(self):
        with open('Allatkert.txt', 'w', encoding='utf-8') as f:
            f.write(f"Növeny: {self.noveny}\n")
            f.write(f"Állatok: {self.allatok}\n")

allatkert = Allatkert(45,67)
allatkert.kiir()
allatkert.kiiras_fajlba()
