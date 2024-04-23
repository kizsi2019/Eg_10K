lista=[]
while True:
    szavak = input("kerek egy szot")
    if szavak=="":
        break

    lista.append (szavak)

print (lista)
legnagyobb= lista[0]
legkissebb=lista[0]
for szo in lista:
    if len(szo) > len(legnagyobb):
        legnagyobb=szo
     
    if len(szo) < len(legkissebb):
        legkissebb=szo
print("lenagyobb: " + legnagyobb)
print("legkisebb: "+ legkissebb)
