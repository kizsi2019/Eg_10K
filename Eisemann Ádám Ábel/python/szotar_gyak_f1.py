konyv = []


while True:
    szerzo = input("Adja meg a könyv szerzőjét: ")
    if szerzo == "":
        break
    cim = input("Kérem adja meg a könyv cimet: ")
    konyv.append({"szerzo": szerzo, "cim": cim})