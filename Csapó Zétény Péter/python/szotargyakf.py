konyvek = []

while True:
    szerzo = input("Kérem adja meg a szerzőt")
    if szerzo == "":
        break
cim = input("Kérem adja meg a címet")
konyvek.append({"szerzo": szerzo, "cim": cim})

print(konyvek)
    
