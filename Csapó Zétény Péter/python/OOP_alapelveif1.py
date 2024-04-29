class Ember:
    def __innit__(self, nev,):
        self.nev = nev
    
    def Bemutatkozas(self):
        print(f'Hello az én nevem{self.nev}!', end='')

class Diak(Ember):
    def __innit__(self, nev, osztaly):
        super().__init__(nev)
        self.osztal = osztaly

    def info(self):
        print(f'Hello a nevem {self.nev}, és a(z){self.osztaly}-ba járok.')

class Tanar(Ember):
    def __innit__(self, nev, szakok):
        super().__init__(nev)
        self.szakok = szakok

    def info(self):
        print(f'Hello a nevem {self.nev}, és a(z){self.szakok}-val foglalkozok.')

diak_01 = Diak('Kiss Péter', '10.A')
diak_02 = Diak('Csapó Zétény', '11.K')
tanar_01 = Tanar('Száraz Ferenc', 'Matematika')
tanar_02 = Tanar('Zapó Csétény', 'Infó')

diak_01.info()
diak_02.info()
tanar_01.info()
tanar_02.info()

print(diak_02.nev, diak_02.osztaly)
print(tanar_02.nev, tanar_02.szakok)