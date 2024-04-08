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


class Tanar:


    def __init__(self,nev,szak):
        self.nev = nev
        self.szak = szak

    def info(self):
        return f'Szia, {self.nev} vagyok, {self.szak} szakos'


tanar_01 = Tanar('Bendeguz', 'Torténelem')
tanar_02 = Tanar('Adam', 'Matek')
print(tanar_01.info())


