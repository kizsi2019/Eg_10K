mondat = input('Adj meg egy mondatot: ')

if mondat[-1] == '?':
        print('Ez a mondat kérdő mondat')
elif mondat[-1] == '.':
    print('Ez egy mondat')
elif mondat[-1] == '!':
    print('ez a mondat felkiáltó,felszólitó ')
else:
    print('nincs befjezve mondat')