'''eletkor=int(input("Add meg az életkorod!"))

if eletkor < 0:
    print("Az életkor nem lehet negatív")
elif eletkor < 18:
    print("Ön még kiskorú")

elif eletkor >= 18:
    print("Ön már felnőtt")
elif eletkor >= 65:
    print("Ön már nyugdíjas")
else:
    print(eletkor)'''
    


eletkor = int(input("Add meg az életkorod: "))

if eletkor < 0:
    print("Az életkor nem lehet negatív!")
elif eletkor < 18:
    print("Ön még kiskorú!")
elif eletkor < 65:
    print("Ön már felnőtt!")
else:
    print("Ön már nyugdíjas!")