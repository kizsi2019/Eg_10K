import random

class kutya:
    nem=['him ', 'nosteny']
    def  __init__(self, nev):
        self.nev=nev
        self.eletkor=random.randit(1,15)
        self.nem= random.choice(self.nem)
def info(self):
    return f"nev: {self.nev}, eletkor:{self.eletkor}, neme{self.nem}"


kutyak_szam=int(input("Kerem a kutyak szamat: "))
kutyak=[]
for i in range(kutyak_szam):
    nev=input(f"kerem a {i+1}, kutya nevet")

print("a kutya adat")
for kutya in kutyak:
    print(kutyak.info())