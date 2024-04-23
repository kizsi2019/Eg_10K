#1.
honapok = ['január', 'február','március', 'április', 'május', 'június'] 
  
index = 1
for honap in honapok:
    print(index, honap)
    index = index +1

#2.
honapok = ['január', 'február','március', 'április', 'május', 'június']
  
for index in range(len(honapok)):
    print(index, honapok[index])
#3. 
  
honapok = ['január', 'február','március', 'április', 'május', 'június']
  
for index, honap in enumerate(honapok):
    print(index, honap)
  