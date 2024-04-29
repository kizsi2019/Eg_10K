class Kor:
    pi = 3.1415

    def __init__(self, r):
        self.r = r

    def terulet(self):
        return self.pi * self.r**2
    
    def kerulet(self):
        return 2*self.r*self.pi


r = float(input("Kérem a kor sugarat: "))
kor = Kor(r)
print(f"A kör terulet: {kor.terulet()} ")
print(f"A kör terulet: {kor.kerulet()} ")
