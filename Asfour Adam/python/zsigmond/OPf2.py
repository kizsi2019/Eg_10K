import random

class Kutya:
    nem = ['him', 'nosteny']

    def __init__(self,nev):
        self.nev = nev
        self.eletkor = random.randint(1, 15)
        self.nem = random.choice(self.nem)

    
    def info(self):
        return f"Nev: {self.nev}, Életkor: {self.eletkor}, Neme: {self.nem}"


kutyak_szama = int(input("Kerem adja meg a kutyak szamat:"))
kutyak = []
for i in range(kutyak_szama):
    nev= input(f"Kerem adja meg a(z) {i+1}. kutya nevet!")
    kutyak.append(Kutya(nev))

print("A megadott kutyak adatai:")
for kutya in kutyak:
    print(kutya.info())