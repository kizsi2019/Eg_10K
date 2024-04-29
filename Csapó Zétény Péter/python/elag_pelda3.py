import random

gondolt_szam = random.randint(1,5)

szam = int(input("Adj egy számot!"))
if szam == gondolt_szam:
    print("Eltaláltad")
elif szam > gondolt_szam:
    print("Nagyobb, mint gondoltam")
else:
    print("Kisebb számra godoltam")
print("Erre a számra gondoltam: ", gondolt_szam)