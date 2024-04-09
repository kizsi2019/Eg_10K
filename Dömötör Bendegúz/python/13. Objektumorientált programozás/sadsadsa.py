import datetime

class Diak:
    def __init__(self, nev, szuletesi_ev, osztaly):
        self.nev = nev
        self.szuletesi_ev = szuletesi_ev
        self.osztaly = osztaly
        

        def eletkor(self):
            return datetime.datetime.now().year - self.szuletesi_ev

        def info(self):
            return f'Szia, {self.nev} vagyok, {self.osztaly} -ba/be járok {self.eletkor()} idos vagyok'
diak_01 = Diak("Nagy Bálint","11.F",2003)
print(diak_01.info())