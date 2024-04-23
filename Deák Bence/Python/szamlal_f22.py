szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']

darab = 0

for i in szavak:
    if i[0] == "e" or i[0] == "E":
        darab += 1
        print(i)
print(f"Feltételnek megfelelő szavak száma: {darab}")
