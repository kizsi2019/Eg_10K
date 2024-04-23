
szavak = ['asztal', 'lámpa', 'ablak', 'kutya', 'alma', 'kukta']
talalat = False

for szo in szavak:
    if szo[0] == 'a' and szo[-1] == 'a':
        talalat = True
        print('Van olyan szó, amelyik "a"-val kezdődik és végződik!')
        break
else:
    # akkor hajtódik végre, ha a ciklus futása nem szakadat meg break-kel
    # tehát az összes listaelem bejárásra került
    print('Nincs ilyen szó!')
