import random

class Diak:
    osztalyok = ['1.A', '1.B', '2.A', '2.B', '3.A', '3.B']
    nevek = ['Kiss Péter', 'Nagy Zsófia', 'Varga Dániel', 'Tóth Anna', 'Horváth Márton', 'Szabó Eszter']
    
    def __init__(self, nev=None, osztaly=None, szul_ev=None):
        if nev is None:
            vezeteknev, keresztnev = random.choice(self.nevek).split()
            self.nev = f"{vezeteknev} {keresztnev}"
        else:
            self.nev = nev
        
        if osztaly is None:
            self.osztaly = random.choice(self.osztalyok)
        else:
            self.osztaly = osztaly
        
        if szul_ev is None:
            self.szul_ev = random.randint(2005, 2010)
        else:
            self.szul_ev = szul_ev
        
        self.kor = self.age()
        
    def age(self):
        return 2023 - self.szul_ev