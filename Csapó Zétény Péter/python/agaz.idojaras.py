import random

class IdojarasAdat:
    def __init__(self, varos, homerseklet, elorejelzes):
        self.varos = varos
        self.homerseklet = homerseklet
        self.elorejelzes = elorejelzes

    def informacio_megjelenites(self):
        print("Varos: ", self.varos)
        print("Jelenlegi hőmérséklet: ", self.homerseklet, "Celsius fok" )
        print("Időjárási előrejelzés: ", self.elorejelzes)

def idojaras_elorejezles_megszerzes(varos):
    #egyszerűen generálunk egy időjárási előrejelzést
    elorejelzesek = ["Napos", "Felhős", "Esős", "Havas", "Ködös"]
    return random.choice(elorejelzesek)

def atlaghomerseklet_megfigyelese(varos):
    #egyszerűen generálunk egy véletlenszerű hőmérsékletet
    return random.randint(10, 25)

#1. feladat
print('1 feladat:')
kivalasztott_varos = input("Válassz egy várost a listából: ")
elorejelzesek = ["Napos","Felhos","Havas","Ködös","Esős"]
elorejelzes = random.choice(elorejelzesek)
print("Az időjárás előrejelzése ", kivalasztott_varos + "-ra", elorejelzes)

#2. feladat
print('2. feladat:')
varos = input("Add eg a várost amelynek az átlaghőmérsékletét szeretnéd megtudni")
atlaghomerseklet = atlaghomerseklet_megfigyelese(varos)
print("Az átlaghőmérséklet ", varos +"-ban", atlaghomerseklet, "Celsius-fok")

#3. feladat
print('3. feladat:')
varos_nev = input("Add meg a város nevét: ")
jelenlegi_homerseklet = atlaghomerseklet_megfigyelese(varos_nev)
idojaras_elorejezles = idojaras_elorejezles_megszerzes(varos_nev)

idojaras_adat = IdojarasAdat(varos_nev, jelenlegi_homerseklet, idojaras_elorejezles)
idojaras_adat.informacio_megjelenites()