import random
class kutya:
    nem = ['hím', 'nosteny']

    def _init_(self, nev):
        self.nev = nev
        self.eletkor = random.randint(1.15)
        self.nem = random.choice(self.nem)

    def info (self):
        return f"Név: {self.nev}, Életkor: {self.eletkor}, Neme: {self.nem}"

kutyak_szama = int(input('Kérem adja meg a kutyák számát'))
kutyak = []
for i in range(kutyak_szama):
    nev = input(f"Kérem adja meg a(z) {i+1}, kutya nevét!")
    
    kutyak.append(kutya(nev))

print("A megadott kutyák információi: ")