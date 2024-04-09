konyvek = []

while True:
    szerzo = input("Kérem adja meg a könyv szerzőjét (ha befejezte enter)")
    if szerzo == "":
        break
    cím = input("kérem adja meg a könyv címét:")
    konyvek.append({"szerzo:" szerzo, "cím:" cím })
print(konyvek)