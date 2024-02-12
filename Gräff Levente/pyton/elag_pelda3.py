import random
gondolt_szam =random.randint(1,5)
szam= int(input("adj szam"))
if szam == gondolt_szam:
    print("jo")
elif szam > gondolt_szam:
    print("nagyobb")
else:
    print("kissebb")
print("erre gondolam:", gondolt_szam)
