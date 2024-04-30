import random

gepszam = random.randint(0, 100)
userszam = int(input("Kérek egy számot 0 és 100 között: "))

if gepszam == userszam:
    print("Gratulálok, eltaláltad! UwU")
elif gepszam > userszam:
    print("Nagyobb számra gondoltam! UwU")
else:
    print("Kisebb számra gondoltam! UwU")
print(f"Erre a számra gondoltam: {gepszam}")
