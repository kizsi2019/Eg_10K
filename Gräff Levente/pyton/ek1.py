import random
lista=[]
for i in range(5):
    szam=random.randit(1,7)
    lista.append(szam)
    
szam2=int(input)("adj egy szamot")


talalat = False
index = 0
while index < len(lista) and not talalat:
	if lista[index] == szam2:
		talalat = True
index = index + 1
print(lista)
if talalat:
    print("van")
else:
    print("nincs")
    