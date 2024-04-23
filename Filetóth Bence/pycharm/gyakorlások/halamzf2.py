import random
halmazhuh = set()
halmaztipp = set()

for i in range(5):
    szam = random.randint(1, 10)
    halmazhuh.add(szam)

for i in range(5):
    szam = int(input("Gibb a nummer: "))
    halmaztipp.add(szam)

szamok ={1,2,3,4,5,6,7,8,9,10}

print(halmazhuh)
print(halmaztipp)
print(halmazhuh & halmaztipp)
print(halmazhuh ^ halmaztipp)
print(szamok - (halmazhuh | halmaztipp))

