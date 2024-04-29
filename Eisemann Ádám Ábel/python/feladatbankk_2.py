class Haromszog:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def kerulet(self):
        return self.a + self.b + self.c

    def terulet(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


a = float(input("Kérem a 'a' haromszogoldalat: "))
b = float(input("Kérem a 'b' haromszogoldalat: "))
c = float(input("Kérem a 'c' haromszogoldalat: "))
h = Haromszog(a,b,c)


print(f"A haromszog keurulete: {h.kerulet()} cm")
print(f"A háromszög területe: {h.terulet()} cm")