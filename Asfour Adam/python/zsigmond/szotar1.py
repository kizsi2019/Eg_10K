
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

# szótár elemeinek elérése kulcs alapján
print(diak['eletkor'])
print(diak.get('eletkor'))

# ilyenkor a megadott alapértékkel tér vissza
print(diak.get('kollegista', 'nem'))

# ellenőrzés, hogy létezik-e a kulcs
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