import datetime

class Diak:
    def __init__(self, nev, osztaly, szuletesi_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szultesi_ev = szuletesi_ev


    def eletkor(self):
        return datetime.datetime.now().year - self.szultesi_ev

    def info(self):
        return f'Szia, {self.nev} vagyok, a {self.osztaly} osztalyba járok, {self.eletkor()} éves vagyok.'


diak_01 = Diak('Kiss Péter', '10.A', 2008)
print(diak_01.info())