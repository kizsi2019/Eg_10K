class negyzet:
    def __init__(self, hossz):
        self.hossz=hossz

    def terulet(self):
        return self.hossz * self.hossz

    def kerulet(self):
        return self.hossz * 4

    def info(self):
        print(f'A(z) {self.hossz} egység sugaru,negyzet területe {self.terulet():.2f} kerülete {self.kerulet():.2f} egység.')




































negyzet_01 = negyzet(10)
print(negyzet_01.kerulet())
print(negyzet_01.terulet())
print(negyzet_01.info())