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

    if szam < legkisebb and szam % 2==0:
        legkisebb=szam
    if szam > legnagyobb and szam % 2==0:
        legnagyobb=szam
print