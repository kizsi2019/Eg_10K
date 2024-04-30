# üres szótár létrehozása
raktar = {}
print(raktar)

# szótár létrehozása adatokkal
diak = {
    'vezeteknev': 'Kiss',
    'keresztnev': 'Péter',
    'eletkor': 17,
    'menza': True
}
print(diak)

print(diak.get('eletkor'))

print(diak.get('kollegista', 'nem'))

print('keresztnev' in diak)

diak['eletkor'] = 17+4
print(diak['eletkor'])

diak['osztaly'] = '10.A'

for kulcs in diak:
	print(kulcs, diak[kulcs])

for ertek in diak.values():
    print(ertek)

for kulcs, ertek in diak.items():
    print(kulcs, ertek)