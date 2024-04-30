
    
    # halmaz létrehozása
reggeli = {'tea', 'vaj', 'piritós'}
    
    # üres halmaz létrehozása
    # ebed = {}  <- SZÓTÁRT hoz létre!!!
ebed = set()

    # bejárható gyűjteményből, pl. listából
ebed = set(['halászlé', 'kenyér', True])  
  

    # egy elem hozzáadása
reggeli.add('lekvár')

    # egy nem meghatározott elem eltávolítása
reggeli.pop()
    
    # egy bizonyos elem eltávolítása
    # ha nincs ilyen elem, akkor hibát eredményez
reggeli.remove('sajt')

    # egy bizonyos elem eltávolítása
    # ha nincs ilyen elem, nem eredményez hibát
reggeli.discard('sajt')
    

reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
ebed = {'víz', 'halászlé', 'kenyér'}

    # metszet
print(reggeli & ebed)
    # unio
print(reggeli | ebed)
    # különbség
print(reggeli - ebed)
    # csak az egyikben, vagy csak a másikban
print(reggeli ^ ebed)
    
      
  
import random
kitalalando = set()
tipp = set()

for i in range(5):
    szam = random.randint(1,10)
    kitalalando.add(szam)

for i in range(5):
    szam = int(input("adj meg egy szamot"))
    kitalalando.add(szam)

szamok = (1,2,3,4,5,6,7,8,9,10)

print(kitalalando)
print(tipp)

print(kitalalando & tipp)
print(kitalalando ^ tipp)
print(kitalalando - (kitalalando | tipp))



    
    # tuple létrehozása
kozeppont = (0, 5)
    
    # de ez is tuple-t eredmenyez
kozeppont = 0, 5

    # hivatkozás a tuple egy elemére
print(kozeppont[1])  # 5
    
    # tuple "kicsomagolása"
x, y = kozeppont  # x értéke: 0, y értéke: 5
  
