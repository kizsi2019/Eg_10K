try:
    oszto = int(input('Mennyivel osszam el a 10-et? '))
    print(f'Az eredmeny: {10 / oszto}')
except (ZeroDivisionError, ValueError) as e:
    print('Hiba: ', e)
print('A program vége')
