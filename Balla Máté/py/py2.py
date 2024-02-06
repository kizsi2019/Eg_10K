'''
szam = int(input("adjmeg egy szamot"))
darab_karakter = 1
sor = 1
while sor <= szam/2:
      oszlop = 1
      while oszlop <= darab_karakter:
          print('O ', end='')
          oszlop = oszlop + 1
      print('')
      darab_karakter = darab_karakter + 1
     sor = sor + 1     
darab_karakter = szam/2
sor = 1
while sor <= szam/2:
      oszlop = 1
      while oszlop <= darab_karakter:
          print('O ', end='')
          oszlop = oszlop + 1
      print('')
      darab_karakter = darab_karakter - 1
      sor = sor + 1     
    

honapok = ['január', 'február','március', 'április']


print(honapok)

print(', '.join(honapok))
  
print(len(honapok))

print(honapok[0])
 
print(honapok[3])
  
print(honapok[1:3])

print(honapok[:3])
 
print(honapok[2:])

print(honapok[-1])      
  
gyumolcsok = []
  

gyumolcs = None
while gyumolcs != '':
    gyumolcs = input('Adj meg egy gyümölcsöt! ')
    if gyumolcs != '':
      # hozzáfűzi a listahoz
      gyumolcsok.append(gyumolcs)
  
  print(gyumolcsok)  
 
import random

lista = []
 
for i in range(10):
    szam = random.randint(1,50)
    if ( szam % 4 == 0):
        print(szam)
    lista.append(i)

tantargyak = ['matek', 'töri', 'bio', 'kémia', 'info']

for tantargy in tantargyak:
	print(tantargy)

 # 0 -> 9
for i in range(10):
    print(i)

  # 5 -> 8
for i in range(5,9):
    print(i)

  # 3 -> 20-ig 6-osával
for i in range(3,21,6):
    print(i)


honapok = ['január', 'február','március', 'április', 'május', 'június'] 
  
index = 0
for honap in honapok:
  print(index, honap)
  index = index + 1
  

  
honapok = ['január', 'február','március', 'április', 'május', 'június']
  
for index in range(len(honapok)):
    print(index, honapok[index])
  

honapok = ['január', 'február','március', 'április', 'május', 'június']
  
for index, honap in enumerate(honapok):
  print(index, honap)
a = []



szam_lista = []
for i in range(1,41):
  if i % 3 ==0:
      szam_lista = i
      print(szam_lista)


szavak = ['asztal', 'lámpa', 'ablak', 'kutya', 'alma', 'kukta', 'tesla']
T_lista = []
for szavak in szavak:
  if szavak[0] == 't' or szavak[0] == 't':
    T_lista.append(szavak)
  print(T_lista)

szamok = [1120,66,125,4,463,8,563,45]

for szam in szamok:
  if szam % 3 == (0 and szam % 2 ==0):
    print(szam)



    # Szövegek (sztringek) összefűzhetőek
print('Jöttem' + ' ' + 'láttam' + ' ' + 'győztem.')

    # Szövegek (sztringek) szorzásjellel megsokszorozhatóak
print('ja' + 'j' * 7)

    # Más adattípusok szöveggé (sztringgé) alakíthatóak az str() függvénnyel
print(str(7.53))
  
sztring = 'Ismered ezt a számot?'

    # Index-szel hivatkozhatunk egy elemükre
print(sztring[0])      # I
print(sztring[-1])     # ?

    # Szeletelhetjük ezeket is 
print(sztring[2:11])
print(sztring[:9])
print(sztring[7:])

    # Meghatározhatjuk a hosszukat
print(len(sztring))

    # for-ciklussal is bejárhatóak
szamlalo = 0
for betu in sztring:
  if betu == 'e' or betu == 'E':
    szamlalo += 1
print(f'A sztringben {szamlalo} db e/E betű van.')

    # Ezeknél is használható az in operátor
if 'e' in sztring:
        print('Van benne e betű.')
else:
        print('Nincs benne e betű.')

mondat = input('adj meg egy mondatot!')
if mondat[-1] == '?':
  print('Ez egy kérdő mondat')
elif mondat[-1] == '.':
  print('Ez egy mondat')
elif mondat[-1] == '!':
  print('Ez felkiáltó/felszolító/mondat')
else:
  print('Nincs befejezve a mondat')


sztring = 'aLmafA' 
        
      # Az első betűt nagybetűvé alakítja,
      # de csak a kiírás erejéig, maga a sztring nem változik, 
      # hiszen a sztringek elemei nem változtathatóak meg!
print(sztring.capitalize())

      # Csupa nagybetűssé alakítja a sztringet
print(sztring.upper())

      # Csupa kisbetűssé alakítja a sztringet
print(sztring.lower())

      # Megszámolja, hányszor fordul elő a megadott karakter
print(sztring.count('a'))

      # Megadja, hányadik indexű helyen fordul elő először a megadott karakter
print(sztring.find('a'))

      # True-val tér vissza, ha a sztring minden eleme kisbetű 
print(sztring.islower())

      # True-val tér vissza, ha a sztring minden eleme nagybetű 
print(sztring.isupper())
    


nyelvek = ['Python', 'C', 'C++', 'Java']

    # sorbarendezi a listát
nyelvek.sort()

    # fordított sorrendbe rendezi a listát
nyelvek.reverse()  
  

    # az adott elem első előfordulásának indexe
print(nyelvek.index('C'))

    # az adott elem hányszor fordul elő
print(nyelvek.count('Python'))

    # NEM listametódus, de így lehet eldönteni, hogy egy elemet tartalmaz-e a lista
print('C++' in nyelvek)

szinek = []

szin = input('adj meg egy színt')
for szin in szinek:
  print(szinek)
else:
  szinek.append(szin)
print(szinek)


nyelvek = ['Python', 'C', 'C++', 'Java']

    # sorbarendezi a listát
nyelvek.sort()

    # fordított sorrendbe rendezi a listát
nyelvek.reverse()  
  

    # az adott elem első előfordulásának indexe
print(nyelvek.index('C'))

    # az adott elem hányszor fordul elő
print(nyelvek.count('Python'))

    # NEM listametódus, de így lehet eldönteni, hogy egy elemet tartalmaz-e a lista
print('C++' in nyelvek)


    # a lista végére hozzáfűz egy elemet
nyelvek.append('Python')
    
    # a listát másolja
nyelvek_masolat = nyelvek.copy()
    
    # a lista végére hozzáfűz egy másik gyűjteményt (pl. listát)
nyelvek_honlapkesziteshez = ['HTML', 'CSS', 'JavaScript']
nyelvek.extend(nyelvek_honlapkesziteshez)
    
    # adott indexű helyre beszúrja a megadott elemet
nyelvek.insert(1, 'Go')     


    # eltávolítja a legutolsó elemet, és azzal tér vissza
    # itt például a törölt értéket a 'torolt_nyelv' fogja tartalmazni
nyelvek.pop()
torolt_nyelv = nyelvek.pop()

    # eltávolítja a megadott indexű elemet,  és azzal tér vissza
nyelvek.pop(1)

    # eltávolítja a megadott indexű elemet
del nyelvek[1]

    # eltávolítja a megadott elemet az elsőként megtalált pozícióból
nyelvek.remove('Python')

    # törli a listát
nyelvek.clear()
#######################

napi_ertekesitesek = [3, 12, 3, 4, 7, 15, 1]

osszesen = 0
for ertekesites in napi_ertekesitesek:
	  osszesen = osszesen + ertekesites

print("A héten ennyi értékesítés történt: ", osszesen)


print('Ez a program kiszámolja az átlagodat.')
print('Ha már nem akarsz több jegyet megadni, írj 0-át!')
print('--------------------------------------------')

darab = 0
osszeg = 0

erdemjegy = int(input('Add meg az első érdemjegyet: '))
while erdemjegy != 0:
  darab = darab + 1
  osszeg = osszeg + erdemjegy
  erdemjegy = int(input('Add meg az következő érdemjegyet: '))
	
if darab != 0:
	print('A jegyeid átlaga: ', osszeg / darab)
else:
	print('Nem adtál meg egy jegyet sem!')
  

lista = [2, 5, 4, 8, 9, 11, 10, 12]
    
talalat = False
index = 0
while index < len(lista) and not talalat:
  if lista[index] % 3 == 0:
    talalat = True
    index = index + 1
    
  if talalat:
    print('Van a listában hárommal osztható szám.')
  else:
    print('Nincs a listában hárommal osztható szám.')

import random

lista = []
osszeg = 0
for i in range(5):
  szam = random.randint(1,10)
  lista.append(szam)
  if szam % 2 ==0:
    osszeg += szam
print(lista)
print(osszeg)

szamok = []
osszeg = 0 
bszam = int(input('adj meg egy szamot -5 és 5 között'))
while(-5 <=bszam <= 5):
  szamok.append(bszam)
  osszeg +- bszam
  bszam = int(input("adj meg egy szamot"))

print(f"a szamok:{szamok}")
print("Az osszeguk:",osszeg)
'''

'''
    Az ELDÖNTÉS esetében azt vizsgáljuk,
    hogy szerepel-e egy bizonyos tulajdonságú elem az adatsorban (itt a listában).
    
    A program azt vizsgálja, hogy van-e hárommal osztható szám a listában.
    

import random 
list = []
for i in range(5):
  szam = random.randint(1,7)
  list.append(szam)

szam2 = int(input("adj meg egy szamot"))

if szam2 in list:
  print("ez a szam már benne van a listaban")
else:
  list.append(szam2)
  print(list)



szo = input(str("adj meg egy szót"))

for i in szo:
  print(i)

szo2 = ("asztal")
betu = input("Adj meg egy betut")
index = 0
talalat = 0
while index < len(szo2) and not talalat:
  if betu in szo2:
    print("talalt") 
    break
  

    A SZÁMLÁLÁS esetében azt vizsgáljuk, hogy egy bizonyos tulajdonságú elemből 
    hány darab van az adatsorban (itt a listában).

    A program azt vizsgálja, hogy hány darab hárommal osztható szám van a listában.
   
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

darab = 0
for szam in lista:
	if szam % 3 == 0:
		darab = darab + 1

print('A listában lévő hárommal osztható számok száma: ', darab)  
  


import random

list= []
list_paros= []
for i in range(5):
  szam = random.randint(1,10)
  list.append(szam)
  if szam % 2 == 0:
    list_paros.append(szam)

print(list)
print(list_paros)
 '''
'''
szavak = ["alma","retek","répa","mogyoro","asztal"]
darab = 0 
for betu in szavak:
  if betu[0] == "a" or betu[0] == "A":
    darab = darab + 1
    print(betu)
print(darab)

talalat = False
index = 0
while index < len(szavak) and not talalat:
        if szavak[index]  == 0:
            talalat = True
        index = index + 1 

'''
'''
    A SZÉLSŐÉRTÉK MEGHATÁROZÁSA esetében azt vizsgáljuk, hogy melyik a legkisebb, 
    illetve a legnagyobb érték az adatsorban (itt a listában).
'''
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

legkisebb = lista[0]
legnagyobb = lista[0]
for szam in lista:
	if szam < legkisebb:
		legkisebb = szam
	if szam > legnagyobb:
		legnagyobb = szam

print(f'A legkisebb szám a listában: {legkisebb}')
print(f'A legnagyobb szám a listában: {legnagyobb}')  

lista = []
szam = input("Adj meg eg szamot")
while szam !="x" or szam !="X" :
  if int(lista) % 2 ==0:
    lista.append(int(szam))
  szam = input("adj meg egy egész számot")
print(lista)

