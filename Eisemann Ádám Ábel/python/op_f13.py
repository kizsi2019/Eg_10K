class Negyzet: 

    
    def __init__(self, hossz):
        self.hossz = hossz
        

    def terulet(self):
        return self.hossz * self.hossz

    def kerulet(self):
        return self.hossz * 4

    def info(self):
        print(f'A(z) {self.hossz} egység oldalu, középpontú negyzet területe {self.terulet():.2f} egység, kerülete {self.kerulet():.2f} egység.')  
  

negyzet_lista = []
int(input("Adj meg egy oldal hosszat: "))
while hossz !=0:
    negyzet = Negyzet(hossz)
    negyzet_lista.append(negyzet)
    hossz = int(input("Adj meg egy oldal hosszat: "))

for negyzet in negyzet_lista:
    print(negyzet.info)




