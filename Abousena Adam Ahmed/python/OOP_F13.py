class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz

    def kerulet(self):
        return 4 * self.oldalhossz

    def terulet(self):
        return self.oldalhossz ** 2


negyzet_lista = []
hossz = int(input("Add meg a négyzet oldalhosszát!"))
while hossz !=0:
    negyzet = Negyzet(hossz)
    negyzet_lista.append(negyzet)
    hossz = int(input("Add meg a négyzet oldalhosszát"))

for negyzet in negyzet_lista:
    print(negyzet.info())


