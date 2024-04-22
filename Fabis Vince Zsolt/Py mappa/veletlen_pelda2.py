import random 
szam = random.randint(1, 2)
if szam == 1:
    erme = "fej"
else:
    erme = "iras"
bekert = input("fej vagy iras?")
if bekert == erme:
    print("Talált")
else:
    print("Nem találat")