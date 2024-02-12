szam = int(input("adj egy szamot"))

if szam % 4 == 0 and szam % 3 ==0:
  print("osztható 3 mal és 4 el")
if szam % 3 == 0:
  print("osztható 3 mal")
elif szam % 4 == 0:
  print("osztható 4 el")
else:
  print("Nem osztható 4 el és 3 mal")

szam = int(input("adj egy szamot"))

if szam > 0 and szam % 2 == 0:
  print("A szam pozitiv páros")
elif szam < 0 and szam % 2 <= 1:
  print("A szam negativ páratlan")  
  
x = 5
y = -3
  
if x < 0 and y < 0:
  print('mindkettő negatív')
  
if x < 0 or y < 0:
  print('van köztük negatív')
  
if not x <= 0:
  print('x pozitív')     
  








import random

gondolt_szam = random.randint(1,50)

num = int(input("Adj meg egy szamot!"))
if num == gondolt_szam:
  print("Eltaláltam")
elif num > gondolt_szam:
  print("Nagyobbb mint gondoltam")
else:
  print("Kissebb mint gondoltam")
print("Erre a számra gondoltam" , gondolt_szam)





szam = int(input("adj egy szamot"))
if szam < 0:
  print("A szam negativ")
elif szam==0:
  print("A szam nulla")
else:
  print("A szam pozitiv")

import random
szam = random.randint(1, 11)
print(f'A geerált szám: {szam}')   
  
valasz = input("szia jó napod van? (i/n)")
if valasz == 'i':
  print("azjó")
elif valasz == 'n':
  print("ok")
else:
  print("szövegértés 0")



