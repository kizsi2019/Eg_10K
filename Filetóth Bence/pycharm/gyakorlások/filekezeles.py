#fájlkezelés

#megnyitása
# amikor megadjuk a fájlnevet ha nem adunk II egyéb paraméter akkor automatikus II szöveg fájlként
forrasfile = open('forras.txt')

#első teszt
'''for fav in forrasfile:
    print(fav)'''

for fav in forrasfile:
    print(fav.strip())

forrasfile.close