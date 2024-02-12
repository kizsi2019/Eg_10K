import random

gondolt_szam =random.randint(1,5)
szam = int(input("adj megegy számot"))
if szam == gondolt_szam:
    print("Eltaláltad")
elif szam > gondolt_szam:
    print("nagyobb mint gondoltam")
else:
    print ("kisebb mint gondoltam")
print("erre a számra gondoltam:",gondolt_szam)