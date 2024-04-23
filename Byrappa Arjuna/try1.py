try:
    Lista = []
    for szam in range(3):
        input('Adj meg 3 számot')
    Lista.append(szam)
    print(f'A szám{Lista}')
except:
    print('Nem adtál meg számokat')

print(Lista)

