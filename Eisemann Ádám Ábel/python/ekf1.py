import random
list = []
for i in range(5):
    szam = random.randint(1, 7)
    list.append(szam)
szam2 = int(input('Adj meg egy számot'))

találat = False
index = 0
while index < len(list) and not találat:
    if list[index] == szam2:
        találat = True
    index = index +1
print(list)

if találat:
	      print('Van a listában ')
else:
	      print('Nincs a listában.')