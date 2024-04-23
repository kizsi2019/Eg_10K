szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']

darab = 0

for i in szavak:
    if i[0] == "a" or i[0] == "A":
        darab += 1
        print(i)
print(f"Feltételnek megfelelő szavak száma: {darab}")
