
reggeli = {'tea', 'vaj', 'piritós'}
    
    # üres halmaz létrehozása
    # ebed = {}  <- SZÓTÁRT hoz létre!!!
ebed = set()

    # bejárható gyűjteményből, pl. listából
ebed = set(['halászlé', 'kenyér', True])  

reggeli.add('lekvár')

    # egy nem meghatározott elem eltávolítása
reggeli.pop()
    
    # egy bizonyos elem eltávolítása
    # ha nincs ilyen elem, akkor hibát eredményez
reggeli.remove('sajt')

    # egy bizonyos elem eltávolítása
    # ha nincs ilyen elem, nem eredményez hibát
reggeli.discard('sajt')
    
  