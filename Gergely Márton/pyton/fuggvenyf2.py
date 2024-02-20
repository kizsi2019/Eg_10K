lista = [1,2,3,4,10]

def paros_e(lista):
    for elem in lista:
        if elem % 2 == 0:
            return True
    return False
print("Existem numeros pares? ",paros_e(lista))