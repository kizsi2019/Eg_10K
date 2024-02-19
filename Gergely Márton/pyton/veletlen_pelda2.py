import random
szam = random.randint(1, 3)
if szam == 1:
    erme = "fej"
else:
    erme= "írás"

bekert = input("fej vagy írás?")
if bekert == erme:
    print("talalt")
else:
    print("nem talalt")