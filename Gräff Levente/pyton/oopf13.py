
class Square:
    def __init__(self, hossz):
        self.hossz = hossz

    def perimeter(self):
        return 4 * self.hossz

    def area(self):
        return self.hossz ** 2
    
negyzet_lista=[]

hossz= int(input("adj szam"))
while hossz !=0:
    negyzet=negyzet(hossz)
    negyzet_lista.append(negyzet)
    hossz=int(input("adj szam"))
for negyzet in negyzet_lista:
    print(negyzet.info)

