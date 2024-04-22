
raktar = {}
print(raktar)

diak = {
	'vezeteknev': 'Kiss',
	'keresztnev': 'Péter',
	'eletkor': 17,
	'menza': True
    }
print(diak)

print(diak['eletkor'])
print(diak.get('eletkor'))



print(diak.get('kollegista', 'nem'))

print('keresztnev' in diak)


    # érték módosítása
diak['eletkor'] = 21
print(diak['eletkor'])

    # még nem létező kulcs megadása értékkel
diak['osztaly'] = '10.A'

    # kulcs-érték törlése
del diak['vezeteknev']


for kulcs in diak:
	print(kulcs, diak[kulcs])

for ertek in diak.values():
    print(ertek)

for kulcs, ertek in diak.items():
    print(kulcs, ertek)
    

szotar = {
            'kutya_neve' : input("A kutya neve"),
            'eletkor' :input("A kutya életkora"),
            'faj':  input("A kutya fajtája"),
            'ervenyes': input("Rendelkezik érvényes oltással?")
}           
print(szotar)

macska = {
    'neve': input("a macska neve"),
    'életkor': input('macska életkora')


}
print(macska)

mod = input("szeretnéd modósítani a nevét?(i/n)")

if mod == 'i':
    del macska['neve']
    macska = {
    'neve': input("a macska neve"),
}
    print(macska)
else:
    print('ok')

mod2 = input("szeretnéd modósítani az életkorát?(i/n)")
if mod2 == 'i':
    macska = {
    'életkor': input('macska életkora')
}
    print(macska)
else:
    print('ok')

print(macska)

polc = []

polc.append({
        'szerzo': 'William Golding',
        'cim': 'A legyek ura'
    })

polc.append({
        'szerzo': 'Ottlik Géza',
        'cim': 'Iskola a határon'
    })

print(polc)  

[{'szerzo': 'William Golding', 'cim': 'A legyek ura'},  
    {'szerzo': 'Ottlik Géza', 'cim': 'Iskola a határon'}]  
  


    
    # halmaz létrehozása
reggeli = {'tea', 'vaj', 'piritós'}
    
    # üres halmaz létrehozása
    # ebed = {}  <- SZÓTÁRT hoz létre!!!
ebed = set()

    # bejárható gyűjteményből, pl. listából
ebed = set(['halászlé', 'kenyér', True])  
  
print(reggeli)
print(ebed)
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


  
konyv =  []

while True:
    szerzo = input("KÉREM ADJA MEG A SZERZO NEVET")
    if szerzo == "":
        break
    cím = input("cím")
    konyv.append("szerzo",szerzo,"cím",cím)

print(konyv)


 
    
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
    
      
  