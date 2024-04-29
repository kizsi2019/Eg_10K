mondat = input("Adj meg egy mondatot!")

if mondat[-1] == '?':
    print('Ez kérdő mondat')
elif mondat[-1] == '.':
    print ("Ez kijelentő mondat")
else:
    print("Ez vagy felkiálltó, felszólitó, vagy óhajtó")