lista = []
try:
    szam = int(input('Adj meg egy számot! '))
    szam = int(input('Adj meg egy számot! '))
    szam = int(input('Adj meg egy számot! '))
except Exception as e:
    print(e)
    print('Nem számot adtál meg!')
szam = int(szam)
lista.append(int(szam))
print(lista)