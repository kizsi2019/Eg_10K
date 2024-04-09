lista = []
szam= int(input("adj meg egy potitív szamot, ha be akarod fejezni adj meg egy negatív szamot"))
while szam >= 0:
    lista.append(szam)
    szam = int(input("Adj meg egy egy piztiv szamot, ha be akarod fejezni adj meg egy negatív szamot"))
print(lista)

def harommal_oszthatok(lista):
    darab= 0
    for elem in lista:
        if elem % 3 == 0:
            darab += 1
    return darab

print(harommal_oszthatok(lista))