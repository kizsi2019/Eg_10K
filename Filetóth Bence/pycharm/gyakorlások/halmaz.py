
reggeli = {'tea', 'vaj', 'piritós','sajt'}

ebed = set()

ebed = set(['halászlé', 'kenyér', True])

print(reggeli)
print(ebed)

reggeli.add('lekvár')

reggeli.pop()

reggeli.remove('sajt')

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

