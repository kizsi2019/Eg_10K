class Szemely():
    def __init__(self, nev):
        self.nev = nev

    def bemutatkozik(self):
        print(f'Szia a nevem {self.nev}'

class Diák(Szemely):
    def __init__(self, nev, osztaly):
        super().__init__(nev)
        self.osztaly = osztaly


class Tanar(Szemely):
    def __init__(self, nev, szakok):
        super().__init__(nev)
        self.szakok = szakok


diak01 = Diák('Kiss Péter', '10.a')
tanar01 = Tanar('Horvath Zita', ['biologia', 'kémia'])
tanar02 = Tanar('schmidth Emil', ['matematika'])

print(diak01.nev, diak01.osztaly)
