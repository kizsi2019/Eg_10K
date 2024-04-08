import random 
kiatlalando = set()
tipp = set()
for i in range(5):
    szam = random.randint(1,10)
    kiatlalando.add(szam)
print(kiatlalando)
for i in range(5):
    szam = int(input("Adj meg egy szamot: "))
    tipp.add(szam)
szamok = {1,2,3,4,5,6,7,8,9,10}

print(kiatlalando)
print(tipp)


print(kiatlalando & tipp)
print(kiatlalando - tipp)
print(szamok-(kiatlalando|tipp))
    