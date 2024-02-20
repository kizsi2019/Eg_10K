Henrik = input("Jösz ma kosarazni? (i/n)") 
Hanna =  input("Jösz ma kosarazni? (i/n)")

if Henrik == 'i' and Hanna == 'i':
    print("mind a ketten jönnek kosarazni")
elif Henrik == 'n' and Hanna == 'n':
    print("egyikük sem jön kosarazni")
elif Henrik == 'n' and Hanna == 'i':
    print("csak az egyikük jön kosarazni")
elif Henrik == 'i' and Hanna == 'n':
    print("csak az egyikük jön kosarazni")

import random

tip = input("fej vagy írás")
x = random.randint(1,2)

if x %2 ==0:
  print("Fej")
elif x %2 ==1:
  print("írás")

if tip == fej and x %2 ==0:
    print("talált")
elif tip  %2 ==1 and x %2 ==1:
    print("talált")
else:
    print("nem talált")