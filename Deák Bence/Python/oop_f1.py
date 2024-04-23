import datetime


class Diak:
    def __init__(self, nev, osztaly, szuletes):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletes = szuletes

    def eletkor(self):
        return datetime.datetime.now().year - self.szuletes

    def info(self):
        print(
            f"Szia, {self.nev} vagyok, a {self.osztaly} osztályba járok, és {self.eletkor()} éves vagyok.")


diak_01 = Diak("Albrecht Schuch", "67.M", 1861)
diak_02 = Diak("Michael Schummär", "24.C", 1776)
diak_03 = Diak("Acro Bat", "2.A", 2001)
diak_01.info()
diak_02.info()
diak_03.info()
