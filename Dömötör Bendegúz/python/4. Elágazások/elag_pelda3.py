import random
gondoltszam = random.randint(1,5)
szam = int(input("Adj meg egy számot: "))
if szam == gondoltszam:
    print("Teli találat!")
elif szam > gondoltszam:
    print("Nagyobb mint gondoltam")
else:
    print("Kisebb mint gondoltam")
print("Erre a számra gondoltam:", gondoltszam)