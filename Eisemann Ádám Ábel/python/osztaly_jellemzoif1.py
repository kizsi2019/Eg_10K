import datetime


class Diak:
    def __init__(self, nev, osztaly, szuletesi_ev,):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev = szuletesi_ev
        

    def eletkor(self):
        return datetime.datetime.now().year - self.szuletesi_ev
        
    def adatok(self):
        return f'Szia, {self.nev} vagyok, a {self.osztaly} ba jarok, {self.eletkor()} éves vagyok'


diak_01 = Diak('Kiss Péter', '10.A', 2006)
print(diak_01.adatok())

