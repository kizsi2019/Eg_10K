konyvek = []

while True:
    szerzo = input("Kerem,adja meg a konyv szerzojet (ha befejezte,) ")
    if szerzo == "":
        break

    cim = input("Kerem, adja meg a konyv cimet:")
    konyvek.append({"szerzo": szerzo, "cim": cim})

    print konyvek