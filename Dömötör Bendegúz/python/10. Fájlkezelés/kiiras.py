
    # Megnyitási módok:
    # r: olvasás 
    # w: írás, fájlt hoz létre; ha léztezik ilyen nevű fájl már, felülírja az eredetit
    # x: írás, fájlt hoz létre; ha léztezik ilyen nevű fájl már, hibát ad 
    # a: a létező fájl végére hozzáfűz, ha még nem létezik ilyen nevű, akkor létrehozza
    # a+: hozzáfűzést és olvasást is lehetővé tesz

with open('./10. Fájlkezelés/kimenet.txt', 'w', encoding='utf-8') as celfajl:
        print('Ez kerül a fájlba...', file=celfajl)  
  