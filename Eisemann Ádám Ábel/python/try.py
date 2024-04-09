
try:
    szam = int(input('Adj meg egy számot! '))
    print(f'A szam négyzete: {szam ** 2}')
except:
    print('Nem számot adtál meg!')
print('A program vége')




try:
    szam = int(input('Adj meg egy számot! '))
    print(f'A szam négyzete: {szam ** 2}')
except ValueError as e:
    print(e)
    # print(type(e))
    print('Nem számot adtál meg!')
print('A program vége')        
  
  


try:
    szam = int(input('Adj meg egy számot! '))
    print(f'A szam négyzete: {szam ** 2}')
except Exception as e:
    print(e)
    # print(type(e))
    print('Nem számot adtál meg!')
print('A program vége')



try:
    oszto = int(input('Mennyivel osszam el a 10-et? '))
    print(f'Az eredmeny: {10 / oszto}')
except ZeroDivisionError as e:
    print('Hiba: ', e)
    print('Nullával nem oszthatunk!')
except ValueError as e:
    print('Hiba: ', e)
    print('Nem számot adtál meg!')
print('A program vége')
  