class Diak:
    def __init__(self, nev, osztaly):
        self.nev = nev
        self.osztaly = osztaly
    
    def info(self):
        print(f"Szia, a nevem {self.nev}, és a(z) {self.osztaly} osztályba járok.")

class Tanar:
    def __init__(self, nev, szak):
        self.nev = nev
        self.szak = szak
    
    def info(self):
        print(f'Szia, a nevem {self.nev}, {self.szak} szako tanár vagyok.')

diak_01 = Diak('Kiss Péter', '10.A')
tanar_01 = Tanar('Horváth Zita', 'matek')
tanar_02 = Tanar('Tóth Tamás', 'magyar')
diak_01.info()
tanar_01.info()
tanar_02.info()