lista = []

for i in range(3):
    a = input("Kérek egy szót: ")
    if a != "":
        lista.append(a)


def listaszam(lista):
    hossz = lista[0]
    for i in lista:
        if len(i) < len(hossz):
            hossz = i
    print(f"A legrövidebb szó: {hossz}")


listaszam(lista)
