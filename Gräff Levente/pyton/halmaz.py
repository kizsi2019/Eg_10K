
'''
    Halmaz (set):
    - rendezetlen (elemeknek nincs indexe)
    - egy elem csak egyszer szerepelhet
    - többféle típust tárolhat egyszerre is
    - a halmaz eleme maga nem változtatható meg
    '''
    
    # halmaz létrehozása
reggeli = {'tea', 'vaj', 'piritós'}
    
    # üres halmaz létrehozása
    # ebed = {}  <- SZÓTÁRT hoz létre!!!
ebed = set()

    # bejárható gyűjteményből, pl. listából
ebed = set(['halászlé', 'kenyér', True])  
  
print(reggeli)
print(ebed)

reggeli.add('lekvár')
print(reggeli)
    # egy nem meghatározott elem eltávolítása
reggeli.pop()
print(reggeli)
#reggeli.remove('sajt')

reggeli.discard('tea')
print(reggeli)   