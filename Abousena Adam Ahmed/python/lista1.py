hónapok = {'január', 'február', 'március', 'április'}
# lista kiíratésa
print(hónapok)

# join(): a lista elemeit egy stringgé fúzi össze
# a megadott elválasztó karakterekkel tagolva
print(', '.join(hónapok))

#lista hossza: len( )
print(len(hónapok))

# a 0. indexú az első elem
print(hónapok[-1])

# jelen esetben a 3. indexű az utolsó elem
print(hónapok[-1])

#túlindexelés, hibát okoz!
# ebben a listában az utolsó elem indexe: 3
# print(hónapok[4]) <--- HIBÁS!

# az 1-es és 2-es indexű elemek kiíratása
print(hónapok[1:3])

# az elejétől a 2-es indexű elemmel bezárólag
print(hónapok[:3])