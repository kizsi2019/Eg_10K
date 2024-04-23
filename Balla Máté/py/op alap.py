
import datetime


class Gepjarmu:
        def __init__(self, rendszam, ossz_km, kov_szerviz, szakasz_km):
            self.rendszam = rendszam
            self.ossz_km = ossz_km
            self.kov_szerviz = kov_szerviz
            self.szakasz_km = szakasz_km

        def szerviz(self):
            return self.kov_szerviz - datetime.datetime.now().year

        def vissza_km(self):
            return 'Benzines vagy elektromos?'


class Taxi(Gepjarmu):
        def __init__(self, rendszam, ossz_km, kov_szerviz, szakasz_km, fogyasztas=6.0, tank_l=35):
            super().__init__(rendszam, ossz_km, kov_szerviz, szakasz_km)
            self.fogyasztas = fogyasztas
            self.tank_l = tank_l

        def vissza_km(self):
            return round(self.tank_l / self.fogyasztas * 100 - self.szakasz_km)


class ETaxi(Gepjarmu):
        def __init__(self, rendszam, ossz_km, kov_szerviz, szakasz_km, hatotav=600):
            super().__init__(rendszam, ossz_km, kov_szerviz, szakasz_km)
            self.hatotav = hatotav

        def vissza_km(self):
            return self.hatotav - self.szakasz_km
  
  
print(type(5), type(7.2), type('alma'), type(True))
print(type([1, 2, 3]), type((1, 2)), type({'név': 'Aladár'}))


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
    oszto = int(input('Mennyivel osszam el a 10-et? '))
    print(f'Az eredmeny: {10 / oszto}')
except ZeroDivisionError as e:
    print('Hiba: ', e)
    print('Nullával nem oszthatunk!')
except ValueError as e:
    print('Hiba: ', e)
    print('Nem számot adtál meg!')
print('A program vége')


try:
    oszto = int(input('Mennyivel osszam el a 10-et? '))
    print(f'Az eredmeny: {10 / oszto}')
except (ZeroDivisionError, ValueError) as e:
    print('Hiba: ', e)
print('A program vége')
  