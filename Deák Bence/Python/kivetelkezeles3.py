
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
