lista=[]
szam = int(input("Adj meg egy pozitív szamot, ha be akarom fejezni"))
while szam >= 0:
    lista.append(szam)
    szam = int(input("Adj meg egy pozitív szamot, ha be akarod fejezni"))
print(lista)

def harommal_oszthato(lista):
    darab=0
    for elem in lista:
        if elem % 3 == 0:
            darab >= 1
        return darab

print("")