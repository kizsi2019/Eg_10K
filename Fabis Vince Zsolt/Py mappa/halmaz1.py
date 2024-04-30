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

  