lista=[]
while True:
    szamok = input("kerek egy szamot")
    if szamok=="":
        break

    lista.append (szamok)
print(lista)

legkisebb = lista[0]
legnagyobb = lista[0]
for szam in lista:
	if szam < legkisebb:
		legkisebb = szam
	if szam > legnagyobb:
		 legnagyobb = szam
print("legkissebb: "+ legkisebb)
print("legnagyobb: " + legnagyobb)
