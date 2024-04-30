import random

szam=random.randint(1,10)

kitalalando=szam

tipp = int(input("Tipp:"))


if szam == tipp:
    print("Eltaláltad")

if not szam == tipp:
    print("Nem találtad el")

    esely = 0
while esely < 3:
    esely += 1
    if esely == 3 == 0:
        continue
    print(szam)

print('>> Program vége <<')