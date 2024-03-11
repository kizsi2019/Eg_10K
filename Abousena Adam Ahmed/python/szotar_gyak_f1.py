konyvek = []

while True:
    szerzo = input("Írd be a szerző nevét:")
    if szerzo == "":
        break
    cim = input("Add meg a könyvnek a címét")
    konyvek.append({"szerzo": szerzo, "cím": cim})

print(konyvek)
