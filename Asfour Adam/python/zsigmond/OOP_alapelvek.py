
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



gpj_01 = Gepjarmu('P 001', 50000, 2026, 128)
taxi_01 = Taxi('ABC123', 60000,2027,)
etaxi_01 = ETaxi('AAA1', 3500, 2028,225, 700)
print(taxi_01.vissza_km())
print(etaxi_01.vissza_km())