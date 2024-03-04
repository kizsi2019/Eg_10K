import random
kitalalando = set()
tipp = set()

for i in range(6):
    szam = random.randint(1,10)
    kitalalando.add(szam)

for i in range(5):
    szam = int(input("Adj meg egy számot!"))
    tipp.add(szam)

szamok = {1,2,3,4,5,6,7,8,9,10}
print(kitalalando)
print(tipp)

print(kitalalando & tipp)
print(kitalalando ^ tipp)
