class Negyzet:
    def __init__(self, oldal_hossza):
        self.oldal_hossza = oldal_hossza

    def kerulet(self):
        
        return 4 * self.oldal_hossza

    def terulet(self):
      
        return self.oldal_hossza ** 2
    
    def info(self):
        print(f'A(z) {self.oldal_hossza} egység oldala negyzet terulete {self.terulet():.f} egység, kerülete {self.kerulet():.f} egység')
oldal_hossza = 5
negyzet = Negyzet(oldal_hossza)
print(f"A négyzet kerülete: {negyzet.kerulet()}")
print(f"A négyzet területe: {negyzet.terulet()}") 

negyzet_lista = []
hossz = int(input("ad meg a negyzet old hosszát!"))
while hossz != 0:
    negyzet_lista = Negyzet(hossz)
    hossz = int(input("Add meg a negyzet oldalhosszat!"))

for negyzet in negyzet_lista:
    print(negyzet.info)