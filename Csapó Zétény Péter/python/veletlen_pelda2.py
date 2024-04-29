import random

kérdés1=input("Fej vagy Írás?")

random_szam=random.randint(1,2)

if random_szam == 1:
    print("Fej")
if random_szam == 2:
    print("Írás")