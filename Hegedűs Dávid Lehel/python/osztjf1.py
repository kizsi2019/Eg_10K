import datetime

class Diak:
    def __init__(self, nev, osztaly, szuletesi_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev = szuletesi_ev


    def eletkor(self):
        return datetime.datetime.now().year - self.szuletesi_ev

    def info(self):
        return f' Szia,{self.nev} vagyok, a {self.osztaly} osztályba járok, {self.eletkor()} vagyok.'

diak_01 = Diak('Kiss Péter', '10.A', 2008)
print(diak_01.info())

