
try:
    szam = int(input('Adj meg egy számot! '))
    print(f'A szam négyzete: {szam ** 2}')
except ValueError as e:
    print(e)
    
    print('Nem számot adtál meg!')
print('A program vége')        
