eletkor = int(input("kerem az eletkorat: "))
if eletkor < 0 :
    print("Az eletkor nem lehet negati szam.")
elif eletkor < 18:
    print("Ön még kiskoru.")
elif eletkor > 18 and eletkor <65:
    print("ön felnött koru.")
elif eletkor > 66:
    print("Ön idős koru.")

else:
    print("Nem szamot adott meg.")