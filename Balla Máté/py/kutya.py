import random
class Kutya:
    nem = ['hím', 'nőstény']

    def __init__(self, nev):
        self.nev = nev 
        self.elektor = random.randint(1,15)
        self.nem = random.choice(self.nem)

    def info(self):
        return f"Név: {self.nev}, Életkor: {self.elektor},Neme:{self.nem}"

kutyak_szama = int(input('KEREM ADJA MEG A KUTYAK SZAMAT:  '))
kutyak = []
for i in range(kutyak_szama):
    nev = input(f'kerem adja meg a {i+1} kutyák nevet')
    kutyak.append(Kutya(nev))
    
print("A megadott kutyak adatai: ")
for kutya in kutyak:
    print(kutya.info())