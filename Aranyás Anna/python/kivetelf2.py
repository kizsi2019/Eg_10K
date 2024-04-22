try:
    szam1 = int(input('Adj meg egy számot! '))
    szam2 = int(input('Adj meg egy számot! '))
    eredmeny = szam1 / szam2
    print("Az osztás eredménye {:.3f}".format(eredmeny))

except:
    print('Nem számot adtál meg!')