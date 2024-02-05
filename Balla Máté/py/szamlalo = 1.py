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
  