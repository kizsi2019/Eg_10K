lista = [1,2,3,4,10]

def paros_e(lista):
    for elem in lista:
        if elem % 2 == 0:
                print(f"páros számok:  {elem}")
print(paros_e(lista))