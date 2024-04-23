eletkor=int(input("add meg az eletkorod"))
if eletkor < 0:
    print("Az életkor nem lehet negatív")
elif eletkor < 18 and eletkor >0:
    print("ön még kiskorú")
elif eletkor >= 18 and eletkor >65:
    
    
    print("ön idős korú")
