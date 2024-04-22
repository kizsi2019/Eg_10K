import datetime


class diak:
    def __init__(self, nev, osztaly, szuletesiev):
        self.nev=nev
        self.osztaly=osztaly
        self.szuletesiev=szuletesiev
    
    def eletkor(self):
        return datetime.datetime.now().year - self.szuletesiev
    def info(self):
        return f'szia, {self.nev} vagyok, a {self.osztaly} osztalyba járok, {self.eletkor()} eves vagyok'
    
diak_01=diak('Kiss Péter','10.A,2008')
print(diak_01.info())                                                                                               
